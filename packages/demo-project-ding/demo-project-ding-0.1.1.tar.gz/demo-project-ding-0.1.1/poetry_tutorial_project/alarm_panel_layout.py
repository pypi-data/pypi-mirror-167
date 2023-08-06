import dash_bootstrap_components as dbc

from dash import Input, Output,State, callback, html, dcc

# import dash_core_components as dcc



modal_config = [
           dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("报警配置")),
                    dbc.ModalBody(
                        [
                            html.P("请选择报警服务名"),
                            dcc.Dropdown(
                                id='alert_tbl_ServiceName',
                                # value='dt-casting-analysis',
                                # options=charts_biz.get_service_list(),
                                clearable=True,
                                className="dcc_control",
                                multi=False,
                            ),
                            html.Br(),
                            html.P("请输入显示最近多少小时的未处理报警"),
                            dcc.Input(id="filter_hours", type="text", placeholder="", style={'marginRight':'10px'}, value = '1'),
                            html.P("请输入每隔多少分钟刷新一次"),
                            dcc.Input(id="update_cycle", type="text", placeholder="", style={'marginRight':'10px'}, value = '10'),
                        ]
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            "确认", id="confirm", className="ms-auto", n_clicks=0
                        )
                    ),
                ],
                # fullscreen = ['sm-down', 'md-down', 'lg-down', 'xl-down', 'xxl-down'],
                fullscreen = 'xxl-down',
                id="modal_config",
                is_open=False,
                centered=True
            ),
        ]

def alarm_panel_layout_fuc(width = 5, height = 800):
    '''
    width: int, the width of the panel (1-12)
    height: int, the height of the panel in unit px
    
    '''

    print('test ok')

    if width>=4:

        card = dbc.Col(
                    dbc.Container([
                        dcc.Interval(id='interval_1m', interval = 60*1000, n_intervals=0),# ms
                        dcc.Store(id='memory_service_info'),
                        html.Div(children= modal_config),
                        dbc.Button('刷新报警',id= 'apply'),
                        dbc.Button('报警配置',id= 'alarm_config',style={"margin-left": "15px"}),
                        dbc.Button("上次刷新时间：{}，共{}条显示{}条, 点击查询全部".format('xxxxx','xx','xx'), href='https://drive.mo.tesla.cn/alert/list/', outline=True, color="success", className="me-1",style={"margin-left": "15px"}),
                        html.Br(),
                        dbc.Toast(
                            dbc.Container([
                                
                                dbc.Container(
                                    id="card_output", 
                                    ),
                                ],
                                id="my_card", 
                            ),
                            style={'overflow': 'scroll',"maxWidth": "2000px", 'width': 160*width,"height":height},

                        ),]
                    ),
                    width=width,
                )
    else:
         card = dbc.Col(
                    dbc.Container([
                        dcc.Interval(id='interval_1m', interval = 60*1000, n_intervals=0),# ms
                        dcc.Store(id='memory_service_info'),
                        html.Div(children= modal_config),
                        dbc.Row([
                            dbc.Col(
                                dbc.Button('刷新报警',id= 'apply'),
                                width = 4
                            ),
                            dbc.Col(
                                dbc.Button('报警配置',id= 'alarm_config'),
                                width = 4
                            ),
                            ]
                        ),
                        html.Br(),
                        dbc.Row(
                            dbc.Col(
                                dbc.Button("上次刷新时间：{}，共{}条显示{}条, 点击查询全部".format('xxxxx','xx','xx'), href='https://drive.mo.tesla.cn/alert/list/', outline=True, color="success", className="me-1")
                            ),
                        ),
                        html.Br(),
                        dbc.Toast(
                            dbc.Container([
                                
                                dbc.Container(
                                    id="card_output", 
                                    ),
                                ],
                                id="my_card", 
                            ),
                            style={'overflow': 'scroll',"maxWidth": "2000px", 'width': 160*width,"height":height},

                        ),]
                    ),
                    width=width,
                )
        
    return card
