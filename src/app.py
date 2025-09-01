import main
import flet as ft

def app_main(page: ft.Page):
    
    def cpf_tool(n):
        cpf_text = ft.Text(value=f'{main.gerar_cpf()}')
        page.add(cpf_text)

    page.add(ft.Text(value='Gerador/Validador de CPF'))
    
    add_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=cpf_tool)
    


    page.add(add_button)
    

ft.app(target=app_main)
