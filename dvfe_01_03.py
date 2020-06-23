import pandas as pd
import numpy as np
from bokeh.plotting import show, figure, output_notebook, reset_output
from bokeh.models.formatters import NumeralTickFormatter
from bokeh.plotting import show, figure, output_notebook
from bokeh.models.formatters import NumeralTickFormatter

def display_australian_salary():

    def bokeh_hist(df, column, weight_column, bins=20, title='', xaxis='', yaxis='', axis=True, plot_width=600, plot_height=400):

        p = figure(title=title, plot_height=plot_height, plot_width=plot_width,
                   tooltips='$x：$y', tools='pan,save')

        p.title.text_font_size = '12pt'
        p.title.align = 'center'
        p.min_border_left = 35
        p.min_border_bottom = 35
        p.axis.ticker.num_minor_ticks = 0
        p.grid.band_fill_color = None
        if axis == True:
            p.axis.axis_label_text_font_size = "10pt"
            p.axis.major_label_text_font_size = "10pt"
            p.yaxis.axis_label = yaxis
            p.xaxis.axis_label = xaxis
            # p.xaxis.formatter = NumeralTickFormatter(format='$0,0a')
            # p.yaxis.formatter = NumeralTickFormatter(format='0,0a')
        else:
            p.axis.visible = None
        hist, edges = np.histogram(df[column], bins=np.linspace(0, 600000, 31))
        p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
               fill_color="navy", line_color="white", alpha=0.5
              )
        return p

    df = pd.read_csv('australian_salary.csv', encoding='CP1252', index_col=0)
    # output_notebook()
    show(bokeh_hist(df, 'average_taxable_income', 'individuals',
                    xaxis='平均纳税收入（加元 AUD/年）',
                    yaxis='职业计数（个）',
                    bins=30))
display_australian_salary()

