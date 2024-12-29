from rest_framework import serializers
from .models import Category, FormFrame, Structure, Product, Material, Affiliation, TempleLength, FrameSize, Collection, SizeBridgeNose


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class FormFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormFrame
        fields = ['name']

class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = ['name']


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['name']


class AffiliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affiliation
        fields = ['name']


class TempleLengthSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempleLength
        fields = ['length']


class FrameSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrameSize
        fields = ['size']


class SizeBridgeNoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeBridgeNose
        fields = ['size']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    form_of_frame = serializers.CharField(source='form_of_frame.name')
    structure = serializers.CharField(source='structure.name')
    material = serializers.CharField(source='material.name')
    affiliation = serializers.CharField(source='affiliation.name')
    temple_length = serializers.CharField(source='temple_length.length')
    frame_size = serializers.CharField(source='frame_size.size')
    size_bridge_nose = serializers.CharField(source='size_bridge_nose.size')
    brand = serializers.CharField(source='brand.name')

    class Meta:
        model = Product
        fields = [
            'id', 'slug', 'name', 'description', 'price', 'stock', 'manufacturer',
            'image', 'category', 'form_of_frame',
            'structure', 'material', 'affiliation', 'temple_length',
            'frame_size', 'size_bridge_nose', 'brand', 'created_at', 'updated_at',
        ]
        read_only_fields = ['slug']