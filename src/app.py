import src.main as main
import flet as ft

def main(page: ft.Page):

    page.add(ft.Text(value='Gerador/Validador de CPF'))
    
    new_task = ft.TextField(hint_text="Digite um CPF:")
    
    page.add(new_task)
    

ft.app(target=main)
