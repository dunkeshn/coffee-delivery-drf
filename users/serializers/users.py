from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from delivery.models.cart import Cart
from users.serializers.profile import ProfileShortSerializer, ProfileUpdateSerializer

User = get_user_model()

class CartShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            'products',
            'sum',
        )


class SubscriptionsShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            ('id', 'username', )
        )


class SubscribersShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            ('id', 'username', )
        )


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
        )

    def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email=email).exists():
            raise ParseError(
                'Почта уже занята.'
            )
        return email

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) # создание пароля с преобразованием в хэш
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'old_password',
            'new_password',
        )

    def validate(self, attrs):
        user = self.instance
        old_password = attrs.pop('old_password')
        if not user.check_password(old_password):
            raise ParseError(
                'Проверьте правильность текущего пароля.'
            )

        return attrs

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def update(self, instance, validated_data):
        password = validated_data.pop('new_password')
        instance.set_password(password)
        instance.save()
        return instance


class MeSerializer(serializers.ModelSerializer):
    profile = ProfileShortSerializer()
    subscribers = SubscribersShortSerializer(many=True)
    subscriptions = SubscriptionsShortSerializer(many=True)
    cart = CartShortSerializer()

    class Meta:
        model = User
        exclude = ('last_login',
                   'is_superuser',
                   'is_staff',
                   'is_active',
                   'date_joined',
                   'groups',
                   'user_permissions',
                   'password',
                   )


class MeUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileUpdateSerializer()
    subscribers = SubscribersShortSerializer(many=True)
    subscriptions = SubscriptionsShortSerializer(many=True)

    class Meta:
        model = User
        exclude = ('last_login',
                   'is_superuser',
                   'is_staff',
                   'is_active',
                   'date_joined',
                   'groups',
                   'user_permissions',
                   'password',
                   )

    def update(self, instance, validated_data):
        # Проверка наличия профиля
        profile_data = validated_data.pop('profile') if 'profile' in validated_data else None

        instance = super().update(instance, validated_data)

        # Update профиля
        if profile_data:
            self._update_profile(instance.profile, profile_data)

        return instance

    def _update_profile(self, profile, data):
        profile_serilizer = ProfileUpdateSerializer(
            instance=profile,
            data=data,
            partial=True
        )
        profile_serilizer.is_valid(raise_exception=True)
        profile_serilizer.save()