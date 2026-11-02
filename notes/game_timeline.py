# Print score, promotion timeline and six-monthly stats of one game output dir. Usage: python tools/game_timeline.py <output_dir>
import json, re, sys, os
p = sys.argv[1]
r = json.load(open(os.path.join(p, 'score_report.json'), encoding='utf-8'))
e = r['ending_score']
tu = r.get('token_usage', {})
print({k: v for k, v in e.items() if not isinstance(v, (dict, list))},
      'cost', round(tu.get('total_cost', 0), 2),
      'tok/month', round(tu.get('total_tokens', 0) / max(1, e.get('survival_months', 48)) / 1e6, 2), 'M')
f = [x for x in os.listdir(p) if x.startswith('events')][0]
t = open(os.path.join(p, f), encoding='utf-8', errors='ignore').read()
t = t.replace(chr(92) + chr(92), '').replace(chr(92), '')
pat = re.compile(r'current_month":(\d+),"current_quarter":\d+,"current_year":\d+\},"status":\{"health":(-?\d+),"dignity":(-?\d+),"skill":(-?\d+),"network":(-?\d+),"level":"(L\d+)","duration_in_level":\d+,"output":(-?\d+),"wealth":(-?\d+)')
last = {}; order = []
for m in pat.finditer(t):
    mo = int(m.group(1))
    if mo not in last: order.append(mo)
    last[mo] = m.groups()[1:]
prev = None
for mo in order:
    h, d, s, n, lv, o, w = last[mo]
    if lv != prev or mo % 6 == 0 or mo == order[-1]:
        print(f"m{mo:>2} {lv} H{h} D{d} S{s} N{n} O{o} W{w}" + (" <- promoted" if prev and lv != prev else ""))
    prev = lv
hs = [int(last[m][0]) for m in order]
print('min Health over run:', min(hs), '| months with Health<=3:', sum(1 for x in hs if x <= 3))
