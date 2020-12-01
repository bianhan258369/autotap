import sys
import os
# current_directory = os.path.dirname(os.path.abspath(__file__))
# root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
root_path = "/Users/bianhan/Desktop/project/autotap/iot-autotap"
sys.path.append(root_path)


from autotapmc.analyze.Fix import generateCompactFix
from autotapmc.model.Tap import ESERule, SERule, SSERule, translateTapToRule, Tap

src = sys.argv[1]
f = open(src, 'r')
ltl_list = []
tap_list = []
while True:
    line = f.readline()
    if line:
        if 'SHOULD NEVER OCCUR TOGETHER' in line:
            states = line.split(' ')[0].split(',')
            ltl = '!F(' + '&'.join(states) + ')'
            ltl_list.append(ltl)
        elif 'SHOULD ALWAYS BE ACTIVE' in line:
            state = line.split(' ')[0]
            ltl = 'G(' + state + ')'
            ltl_list.append(ltl)
        elif 'SHOULD NEVER HAPPEN' in line:
            state = line.split(' ')[0]
            ltl = '!F(' + state + ')'
            ltl_list.append(ltl)
        else:
            if 'WHILE' in line:#IF trigger WHILE condition1,condition2,... THEN action
                trigger = line.split(' ')[1].lower()
                conditions = line.split(' ')[3].lower().split(',')
                action = line.split(' ')[5].lower()
                tap_list.append(Tap(trigger=trigger, condition=conditions, action=action))
            elif 'FOR' in line: #IF trigger FOR time THEN action
                trigger = line.split(' ')[1].lower()
                action = line.split(' ')[5].lower()
                tap_list.append(Tap(trigger=trigger, action=action))
            else: #IF trigger THEN action
                trigger = line.split(' ')[1].lower()
                action = line.split(' ')[3].lower()
                tap_list.append(Tap(trigger=trigger, action=action))
    else:
        break
f.close()
ltl = '!(%s)' % ' & '.join(ltl_list)
useful_tap_list = []
ignored_tap_list = []
for tap in tap_list:
    flag = False
    triggerEntity = tap.trigger.split('=')[0]
    actionEntity = tap.action.split('=')[0]
    if tap.condition == []:
        for tempLTL in ltl_list:
            if triggerEntity in tempLTL or actionEntity in tempLTL:
                useful_tap_list.append(tap)
                flag = True
        if flag:
            continue
    else:
        for condition in tap.condition:
            conditionEntity = condition.split('=')[0]
            for tempLTL in ltl_list:
                if triggerEntity in tempLTL or actionEntity in tempLTL or conditionEntity in tempLTL:
                    useful_tap_list.append(tap)
                    flag = True
            if flag:
                break
        if flag:
            continue
    ignored_tap_list.append(tap)
new_rule_patch = generateCompactFix(ltl, useful_tap_list, init_value_dict={})

for tap in new_rule_patch:
    print(translateTapToRule(tap).log())
for tap in ignored_tap_list:
    print('IF %s THEN %s' % (tap.trigger.strip(), tap.action.strip()))


