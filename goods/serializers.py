from rest_framework import serializers
from .models import Product, Category, Description


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
    description = serializers.ListField(child=serializers.CharField(), required=False)  # Allow a list of descriptions

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        # Extract the nested Category data
        category_data = validated_data.pop('category')
        descriptions_data = validated_data.pop('description', [])

        # Create or retrieve the Category object
        category, _ = Category.objects.get_or_create(**category_data)

        # Create the Product with the associated Category
        product = Product.objects.create(category=category, **validated_data)

        # Create Description instances and associate them with the Product
        for description_text in descriptions_data:
            Description.objects.create(product=product, text=description_text)

        return product

    def to_representation(self, instance):
        """
        Serialize the Product model instance to include the description field.
        """

        representation = super(ProductSerializer, self).to_representation(instance)

        # Fetch and include the descriptions associated with the product
        descriptions = instance.description_set.values_list('text', flat=True)
        representation['description'] = descriptions

        return representation
