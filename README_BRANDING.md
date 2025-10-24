# Branding Pack (Bootstrap + Dash)

Files:
- `app/assets/styles/branding.css` — brand colours + spacing + AG Grid accents.
- `app/component/navbar.py` — purple navbar with logo + dynamic menu.
- `app/component/page_scaffold.py` — consistent page wrapper + KPI card helper.
- `app/pages/style_guide.py` — visual preview page at `/style`.

How to use:
1. Merge `app/` into your project (keep existing files as needed).
2. Place a white transparent logo at `app/assets/logo-white.png`.
3. Ensure your app factory loads Bootstrap + figure template:
   ```python
   import dash_bootstrap_components as dbc
   from dash_bootstrap_templates import load_figure_template
   external_stylesheets = [dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP]
   load_figure_template("bootstrap")
   ```
4. (Optional) Set Plotly default palette:
   ```python
   import plotly.io as pio
   pio.templates["brand"] = pio.templates["bootstrap"]
   pio.templates["brand"].layout.colorway = [
       "#732282", "#00747A", "#002664", "#9C9A00", "#B06F00", "#882345", "#000000"
   ]
   pio.templates.default = "brand"
   ```
