import autotapmc.buchi.Buchi as Buchi
from autotapmc.analyze.Draw import generateGraph
from autotapmc.analyze.Fix import generateFixForSafety, generateCompactFix
from autotapmc.channels.AirConditioner import SimpleAC
from autotapmc.channels.Weather import Weather
from autotapmc.channels.Window import Window
from autotapmc.model.IoTSystem import IoTSystem
import os
import time

from autotapmc.model.Tap import ESERule, SERule, SSERule, translateTapToRule, Tap

try:
    os.stat('my_temp')
except FileNotFoundError:
    os.mkdir('my_temp')


# class MySystem(IoTSystem):
#     weather = Weather()
#     win = Window()
#     ac = SimpleAC()
#     # rule1 = SERule('weather.temperatureGreaterThan25', 'ac.poweron')
#
# ltl_list = ["!F (ac.on & win.open)","!F (weather.raining & win.open)"]
# ltl = '!(%s)' % ' & '.join(ltl_list)
# print(ltl)

# system.transition_system.writeToGv('my_temp/ts.gv')
# ltl = '(F (ac.on & win.open))'


# ltls = list()
# ltls.append('(F (ac.on & win.open))')
# ltls.append('(F (weather.raining & win.open))')
# print(system.transition_system.ap_list)
# ltl = 'F (weather.raining & win.open)'
# ltl = '(F (ac.on & win.open))'
# ts = system.transition_system
# ts.writeToGv('my_temp/ts.gv')
# buchi_ts = Buchi.tsToGenBuchi(ts)
# buchi_ltl = Buchi.ltlToBuchi('!G (weather.raining -> win.closed)')
# (buchi_final, pairs) = Buchi.product(buchi_ts, buchi_ltl)
# generateGraph(system, ltls, 'my_temp/test1')
# system = MySystem()
# system.transition_system.writeToGv('my_temp/ts.gv')
# ltl = '!(!F (ac.on & win.open) & !F (weather.raining & win.open))'
# patch_result = generateFixForSafety(system, ltl)
#
#
# for a in patch_result:
#     for b in a:
#         for c in b:
#             print()
#             print(c.log())

ltl_list = ['!F (thermostat.ac=true & window_liv.open=true)',
            '!F (weather.raining=true & window_liv.open=true)',
            ]
ltl = '!(%s)' % ' & '.join(ltl_list)
print(ltl)
tap_list = [
    Tap(action='window_liv.open=false',trigger='hue_light.color=red'),
    Tap(action='window_liv.open=true', trigger='hue_light.color=green')
    # Tap(action='thermostat.ac=false',trigger='air.temperature<20')
    # Tap(action='window_liv.open=false',trigger='weather.raining=true')
]
starttime = time.time()
new_rule_patch = generateCompactFix(ltl, tap_list, init_value_dict={})
endtime = time.time()
dtime = endtime - starttime
print("程序运行时间：%.8s s" % dtime)  #显示到微秒
for tap in new_rule_patch:
    # print('if ' + tap.trigger)
    # print(tap.condition)
    # print(tap.action)
    # print()
    print(translateTapToRule(tap).log())
