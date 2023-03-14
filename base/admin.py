from django.contrib import admin
from django.contrib import messages
from base.models import Contato

@admin.action(description='Marcar Formulário de Contato como lido')
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request, 'Formulário de Contato marcado como lido', messages.SUCCESS)
    

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data', 'lido']
    actions = [marcar_como_lido]
    


