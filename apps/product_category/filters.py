from django_filters import FilterSet, CharFilter, NumberFilter, ModelChoiceFilter
from .models import *


class ProductFilter(FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        active_filters = ConnectionFilters.objects.filter(active_status='on').values_list('filter_value', flat=True)
        
        for field_name in list(self.filters.keys()):
            if field_name not in active_filters:
                self.filters.pop(field_name)

    name = CharFilter(field_name='name', lookup_expr='icontains', label='Название')
    description = CharFilter(field_name='description', lookup_expr='icontains', label='Описание')
    price_min = NumberFilter(field_name='price', lookup_expr='gte', label='Минимальная цена')
    price_max = NumberFilter(field_name='price', lookup_expr='lte', label='Максимальная цена')
    category = ModelChoiceFilter(queryset=Category.objects.all(), label='Категория')
    manufacturer = CharFilter(field_name='manufacturer', lookup_expr='icontains', label='Производитель')
    form_of_frame = ModelChoiceFilter(queryset=FormFrame.objects.all(), label='Форма оправы')
    structure = ModelChoiceFilter(queryset=Structure.objects.all(), label='Конструкция')
    material = ModelChoiceFilter(queryset=Material.objects.all(), label='Материал')
    affiliation = ModelChoiceFilter(queryset=Affiliation.objects.all(), label='Принадлежность')
    temple_length = ModelChoiceFilter(queryset=TempleLength.objects.all(), label='Длина заушника')
    frame_size = ModelChoiceFilter(queryset=FrameSize.objects.all(), label='Размер рамки')
    size_bridge_nose = ModelChoiceFilter(queryset=SizeBridgeNose.objects.all(), label='Размер переносицы')
    brand = ModelChoiceFilter(queryset=Collection.objects.all(), label='Бренд')

    class Meta:
        model = Product
        fields = []
