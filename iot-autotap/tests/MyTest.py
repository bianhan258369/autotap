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


# PREFERRED Air.temperature IS 20
# IF Light.brightness<35 THEN Light.brightness should increase
# IF Person.distanceFromMc<=2 THEN allow using microphone
# IF Person.distanceFromPro<=2 THEN allow using projector
# IF Projector.pon THEN Blind.bclosed,Window.wclosed
# CO2.ppm SHOULD NEVER BE ABOVE 800
# Air.humidity SHOULD ALWAYS BE ABOVE 70
# Window.wopen,Ac.coldOn SHOULD NEVER OCCUR TOGETHER
# Window.wopen,Ac.hotOn SHOULD NEVER OCCUR TOGETHER

# ltl_list = [
#     '!F (ac.mode=cold & window.on=true)',
#     '!F (ac.mode=hot & window.on=true)',
#     '!F (weather.raining=true & window.on=true)',
#     '!F (window.on=true & projector.on=true)'
# ]

ltl_list = [
    'G(!weather.temperature>25 | thermostat.ac=true)',
    'G(!weather.raining=true | thermostat.ac=false)',
    # 'G (thermostat.ac=true)',
]
ltl = '!(%s)' % ' & '.join(ltl_list)
# print(ltl)
tap_list = [
    # Tap(trigger='air.temperature=over20', action='ac.mode=cold'),
    # Tap(trigger='air.temperature=below20', action='ac.mode=hot'),
    # Tap(trigger='light.brightness=over35', action='bulb.on=false'),
    # Tap(trigger='light.brightness=below35', action='bulb.on=true'),
    # Tap(trigger='person.distanceFromMc=over2', action='microphone.on=false'),
    # Tap(trigger='person.distanceFromMc=below2', action='microphone.on=true'),
    # Tap(trigger='person.distanceFromPro=over2', action='projector.on=false'),
    # Tap(trigger='person.distanceFromPro=below2', action='projector.on=true'),
    # Tap(trigger='co2.ppm=over800', action='af.on=true'),
    # Tap(trigger='co2.ppm=below200', action='af.on=false'),
    # Tap(trigger='air.humidity=below70', action='ah.on=true'),
    # Tap(trigger='air.humidity=over100', action='ah.on=false')
]

useful_tap_list = []
# ignored_tap_list = []
# for tap in tap_list:
#     flag = False
#     triggerEntity = tap.trigger.split('=')[0]
#     actionEntity = tap.action.split('=')[0]
#     for tempLTL in ltl_list:
#         if triggerEntity in tempLTL or actionEntity in tempLTL:
#             useful_tap_list.append(tap)
#             flag = True
#     if flag:
#         continue
#     ignored_tap_list.append(tap)

starttime = time.time()
new_rule_patch = generateCompactFix(ltl, useful_tap_list, init_value_dict={})
endtime = time.time()
dtime = endtime - starttime
print("程序运行时间：%.8s s" % dtime)  #显示到微秒
for tap in new_rule_patch:
    print(translateTapToRule(tap).log())
print()
# for tap in ignored_tap_list:
#     print('IF <%s> THEN <%s>' % (tap.trigger, tap.action))

# print(translateTapToRule(Tap(trigger='air.temperature=over20',condition=['a','b'] ,action='AC.mode=cold')).log())