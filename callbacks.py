#Some callbacks
@app.callback(Output('graph-fig5', 'figure'),[Input('radioitems5', 'value')])

def update_figure(selected_item):
    filtered_df = df_gen_empleo_turismo[df_gen_empleo_turismo['SUBTEMA2'] == selected_item]
    
    if selected_item == "Empleo Turismo Bogotá Trimestral":
    
        fig5 = px.bar(filtered_df, x="MES", y="VALOR", color="MES", facet_col="AÑO",
             title = selected_item,
             labels={
                "MES": "",  "VALOR": "Empleos", "AÑO": ""
            }
            )
    else:
        fig5 = px.line(filtered_df , x="AÑO", y="VALOR", color="VARIABLE", line_group="VARIABLE",
             title = selected_item,
             labels={
                "VALOR": "Empleos", "AÑO": "Año", "VARIABLE" : "Categoría"
            }
            )
    
    if selected_item == "Participación %  ":
        fig5.update_layout(yaxis_title="Porcentaje")
        
    fig5.update_layout(transition_duration = 500)
        
    return fig5

@app.callback(Output('graph-fig4', 'figure'),[Input('radioitems4', 'value')])

def update_figure(selected_item):
    filtered_df = df_conect_internacional[df_conect_internacional['SUBTEMA'] == selected_item]
    variable = filtered_df['VARIABLE'].iloc[0]

    fig4 = px.bar(filtered_df, x="AÑO", y="VALOR", color="AÑO",
             title = variable + " " + selected_item.lower() + " por año",
             labels={
                "VALOR": variable, "AÑO": "Año"
            }
            )

    fig4.update_layout(transition_duration = 500)

    return fig4

@app.callback(Output('graph-fig8', 'figure'),[Input('radioitems8', 'value')])

def update_figure(selected_item):
    filtered_df = df_turismo_internacional[df_turismo_internacional['VARIABLE'] == selected_item]
    clase = filtered_df['CLASE'].iloc[0]
    
    fig8 = px.line(filtered_df , x="AÑO", y="VALOR", color="SUBTEMA", line_group="SUBTEMA",
             title = selected_item,
             labels={
                "VALOR": clase, "AÑO": "Año"
            }
            )
    
    fig8.update_layout(legend_title="Continente",transition_duration = 500)

    return fig8

@app.callback(Output('graph-fig9', 'figure'),[Input('radioitems9', 'value')])

def update_figure(selected_item):
    filtered_df = df_turismo_internacional2[df_turismo_internacional2['VARIABLE'] == selected_item]
    
    fig9 = px.area(filtered_df , x="AÑO", y="VALOR", color="CLASE", line_group="CLASE",
             title = selected_item,
             labels={
                "VALOR": "Participación mundo entero(%)", "AÑO": "Año"
            }
            )
    
    fig9.update_layout(legend_title="Categoría",transition_duration = 500)

    return fig9
