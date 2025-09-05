import main
import flet as ft
import time

def app_main(page: ft.Page):
    
    page.padding = 0
    page.window.width = 420
    page.window.height = 420
    page.padding = ft.padding.only(top=20, left=20, right=20, bottom=20)

    def cpf_tool(e):
        if cpf_field.value == '':                 
            cpf_field.value = main.gerar_cpf()
            update_icon(e)
            page.update()
        else:
            cpf_field.value = main.verificar_cpf(f'{cpf_field.value}')
            page.update()
            time.sleep(1)
            cpf_field.value = ''
            page.update()
            update_icon(e)
    
    def update_icon(e):
        if cpf_field.value == '':
            add_button.icon = ft.Icons.ADD
        else:
            add_button.icon = ft.Icons.CHECK
        page.update()

    page.add(ft.Text(value='Gerador/Validador de CPF', text_align=ft.TextAlign.CENTER, width=300, size=20))
    
    cpf_field = ft.TextField(hint_text='Digite um CPF...', on_change=update_icon, border_radius=10)

    add_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=cpf_tool, bgcolor=ft.Colors.INDIGO)
        

    card = ft.Column(
        width=400,
        controls=[
            ft.Row(
                controls=[
                    cpf_field,
                    add_button
                ]
            )
        ]
    )
    


    page.add(card)
    page.update()
    

ft.app(target=app_main)
