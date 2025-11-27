import flet as ft
import conexao as db

def menu_principal(page:ft.Page, usuario):
    page.clean()

    def ir_produtos(e):
        tela_produtos(page, usuario)

    def ir_estoque(e):
        tela_produtos(page, usuario)

    def logout(e):
        page.window.close()

    header = ft.Row([
        ft.Text(f"Olá, {usuario[1]}", size=20, weight="bold"),
        ft.ElevatedButton("Sair", on_click=logout, bgcolor=ft.Colors.RED_400, color="white")
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    botoes = ft.Column([
        ft.ElevatedButton("📦 Cadastro de Produtos", on_click=ir_produtos, height=60, width=300),
        ft.ElevatedButton("📊 Gestão de Estoque", on_click=ir_estoque, height=60, width=300)], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)
    
    page.add(header, ft.Divider(), ft.Container(content=botoes, padding=50, alignment=ft.alignment.center))