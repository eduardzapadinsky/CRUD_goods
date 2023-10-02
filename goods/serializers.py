from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    """

    category = CategorySerializer()  # Serialize the category field as nested data

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        # Extract the nested Category data
        category_data = validated_data.pop('category')

        # Create or retrieve the Category object
        category, _ = Category.objects.get_or_create(**category_data)

        # Create the Product with the associated Category
        product = Product.objects.create(category=category, **validated_data)

        return product

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)

        # Update fields of the Product instance with the validated data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if category_data:
            category, _ = Category.objects.get_or_create(**category_data)
            instance.category = category

        instance.save()
        return instance
