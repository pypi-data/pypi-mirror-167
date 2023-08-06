import numpy as np
import sympy as sym
import pydae.build_cffi as db
from pydae.bmapu import bmapu_builder


data = {
    "sys":{"name":"smib_syn","S_base":100e6, "K_p_agc":0.0,"K_i_agc":0.0,"K_xif":0.01},  
    "lines":[
        {"bus_j": "1",  "bus_k":  "2", "X_pu":0.01, "R_pu":0.0, "S_mva": 200.0, 'monitor':True}
         ],
    "buses":[
            {"name":  "1", "P_W":0.0, "Q_var":0.0, "pos_x": -1500.0, "pos_y":  200.0, "units": "m", "U_kV":20.0},
            {"name":  "2", "P_W":0.0, "Q_var":0.0, "pos_x":   100.0, "pos_y":    0.0, "units": "m", "U_kV":20.0}
    ],
    "genapes":[{"bus":"2","S_n":1000e6,"F_n":50.0,"R_v":0.01,"X_v":0.1,"K_delta":0.001,"K_alpha":0.00001}],
    "syns":[{"bus":"1","S_n":100e6,
         "X_d":1.8,"X1d":0.3, "T1d0":8.0,    
         "X_q":1.7,"X1q":0.55,"T1q0":0.4,  
         "R_a":0.0025,"X_l": 0.2, 
         "H":5.0,"D":0.5,
         "Omega_b":314.1592653589793,"omega_s":1.0,"K_sec":0.0,
         "K_delta":0.0}  
]}

grid = bmapu_builder.bmapu(data)
grid.checker()
grid.build()

g_list = grid.dae['g'] 
h_dict = grid.dae['h_dict']
f_list = grid.dae['f']
x_list = grid.dae['x']
params_dict = grid.dae['params_dict']


sys = {'name':'smib',
       'params_dict':params_dict,
       'f_list':f_list,
       'g_list':g_list,
       'x_list':x_list,
       'y_ini_list':grid.dae['y_ini'],
       'y_run_list':grid.dae['y_run'],
       'u_run_dict':grid.dae['u_run_dict'],
       'u_ini_dict':grid.dae['u_ini_dict'],
       'h_dict':h_dict}

dblr = db.builder(sys)
dblr.build()

import numpy as np
import matplotlib.pyplot as plt
import ipywidgets
plt.style.use(r'https://raw.githubusercontent.com/jmmauricio/edashboards/main/presentation.mplstyle')
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

import smib
grid = smib.model()


class dashboard(smib.model):
    
    def __init__(self):
        
        super().__init__()
        
        grid = smib.model()
        grid.Dt = 0.01
        grid.decimation = 1
        grid.ini({'p_m_1':0.0,'v_f_1':1.0},'xy_0.json')
        grid.run(20.0,{})
        grid.post();
        
        self.grid = grid
        
        plt.style.use(r'https://raw.githubusercontent.com/jmmauricio/edashboards/main/presentation.mplstyle')
        self.colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
        self.widgets()
        
    def widgets(self):
        
        grid = self.grid
        colors = self.colors

        plt.ioff()
        plt.clf()


        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(9, 4), frameon=False)
        fig.canvas.toolbar_visible = False

        self.line_delta = axes[0,0].plot(grid.Time, grid.get_values('delta_1'), label='$\sf \delta$', color=colors[4])
        self.line_omega = axes[1,0].plot(grid.Time, grid.get_values('omega_1'), label='$\sf \omega$', color=colors[1])
        self.line_v_1 = axes[0,1].plot(grid.Time, grid.get_values('V_1'), label='$\sf V_1$', color=colors[5])
        #line_theta_1 = axes[0,1].plot(T, Y[:,syst.y_list.index('theta_1')], label='$\sf \\theta_1$')
        self.line_p_t = axes[1,1].plot(grid.Time, grid.get_values('p_g_1'), label='$\sf p_s$', color=colors[2])
        self.line_q_t = axes[1,1].plot(grid.Time, grid.get_values('q_g_1'), label='$\sf q_s$', color=colors[0])

        y_labels = ['$\delta$','$\omega$','$P_t$']

        axes[0,0].set_ylim((-1,2))
        axes[1,0].set_ylim((0.98,1.02))
        axes[0,1].set_ylim((0.95,1.05))
        axes[1,1].set_ylim((-0.5,1.5))

        axes[0,0].grid(True)
        axes[1,0].grid(True)
        axes[0,1].grid(True)
        axes[1,1].grid(True)
        axes[0,0].legend(loc='best')
        axes[1,0].legend(loc='best')
        axes[0,1].legend(loc='best')
        axes[1,1].legend(loc='best')

        axes[1,0].set_xlabel('Time (s)')  
        axes[1,1].set_xlabel('Time (s)') 

        fig.tight_layout()
        
        self.fig = fig
        #axes[0].set_title('Par en función de la velocidad')
        #axes[1].set_title('Corriente en función de la velocidad')


        self.sld_p_m = ipywidgets.FloatSlider(orientation='horizontal',
                                        description_allow_html=True,description="p<sub>m</sub>", 
                                        value=grid.get_value('p_m_1'), min=0.0,max= 1.2, 
                                        step=.1)


        self.sld_v_f = ipywidgets.FloatSlider(orientation='horizontal',
                                        description_allow_html=True,description="v<sub>f</sub>", 
                                        value=grid.get_value('v_f_1'), min=0.5,max= 4, 
                                        step=.1)

        self.prog_c = ipywidgets.IntProgress(
            value=100,
            min=0,
            max=120,
            step=1,
            description='SM Load:',
            bar_style='', # 'success', 'info', 'warning', 'danger' or ''
            orientation='horizontal' 
        )

        self.prog_damp = ipywidgets.IntProgress(
            value=10,
            min=0,
            max=20,
            step=1,
            description='ζ = 1.0',
            bar_style='', # 'success', 'info', 'warning', 'danger' or ''
            orientation='horizontal' 
        )
        
    def update(self,change):
        
        grid = self.grid

        p_m = self.sld_p_m.value
        v_f = self.sld_v_f.value


        #grid = smib.smib_class()
        #grid.Dt = 0.01
        grid.decimation = 2
        grid.Dt = 0.01
        grid.ini({'p_m_1':0.0,'v_f_1':1.0},'xy_0.json')
        grid.run( 1.0,{})
        grid.run(10,{'p_m_1':p_m,'v_f_1':v_f})
        grid.Dt = 0.1
        grid.run(20,{'p_m_1':p_m,'v_f_1':v_f})

        grid.post();


        self.line_delta[0].set_data(grid.Time, grid.get_values('delta_1'))
        self.line_omega[0].set_data(grid.Time, grid.get_values('omega_1'))
        self.line_v_1[0].set_data(grid.Time, grid.get_values('V_1'))
        #line_theta_1 = axes[0,1].plot(T, Y[:,syst.y_list.index('theta_1')], label='$\sf \\theta_1$')
        self.line_p_t[0].set_data(grid.Time, grid.get_values('p_g_1'))
        self.line_q_t[0].set_data(grid.Time, grid.get_values('q_g_1'))

        i_d, i_q = grid.get_mvalue(['i_d_1','i_q_1'])
        c = (i_d**2+i_q**2)*0.5*np.sqrt(2)

        self.prog_c.bar_style = 'success'
        if c>0.9:
            self.prog_c.bar_style = 'warning'
        if c>1.0:
            self.prog_c.bar_style = 'danger'
        self.prog_c.value = 100*c

        self.fig.canvas.draw_idle()


    def show(self):

        self.sld_p_m.observe(self.update, names='value')
        self.sld_v_f.observe(self.update, names='value')

        layout_row1 = ipywidgets.HBox([self.fig.canvas])
        layout_row2 = ipywidgets.HBox([self.sld_p_m,self.sld_v_f,self.prog_c])

        layout = ipywidgets.VBox([layout_row1,layout_row2])
        self.layout = layout
        display(self.layout)
     