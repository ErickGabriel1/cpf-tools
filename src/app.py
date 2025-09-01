import main
import flet as ft

def app_main(page: ft.Page):
    
    def cpf_tool(e):
        if cpf_field.value == '':                 
            cpf_field.value = main.gerar_cpf()
            update_icon(e)
            page.update()
        else:
            cpf_field.value = main.verificar_cpf(f'{cpf_field.value}')
            page.update()
    
    def update_icon(e):
        if cpf_field.value == '':
            add_button.icon = ft.Icons.ADD
        else:
            add_button.icon = ft.Icons.CHECK
        page.update()

    page.add(ft.Text(value='Gerador/Validador de CPF'))
    
    cpf_field = ft.TextField(hint_text='Digite um CPF...', on_change=update_icon)

    add_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=cpf_tool)
        

    card = ft.Column(
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
