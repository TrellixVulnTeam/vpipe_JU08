import sys
sys.path.append("..")
from vpipe import Stage
from vpipe import Transformer

def model(criterion, partition, recompute_ratio):
    _declares = get_declares()
    _calculations = get_caculations()
    module = Transformer(_declares, _calculations)
    module.generate_layer_blocks()
    start = 0
    inputs = []
    outputs = [['out333']]
    all_outputs = []
    declares = []
    calculations = []
    for i in partition:
        stage = module.generate_stage(start, start + i)
        start += i
        declares.append(stage[0])
        calculations.append(stage[1])
        inputs.append(stage[2])
        all_outputs.append(stage[3])
    
    for i in range(len(partition)-1, 0, -1):
        previous_output = []
        for name in inputs[i]:
            if name != 'out0' and name != 'out1' and name != 'out2':
                previous_output.append(name)
        for name in outputs[0]:
            if name not in all_outputs[i] and name not in previous_output:
                previous_output.append(name)
        outputs.insert(0, previous_output)

    return [
        (Stage(inputs[0], outputs[0], declares[0], calculations[0], recompute_ratio[0]), replace(inputs[0]), outputs[0]),
        (Stage(inputs[1], outputs[1], declares[1], calculations[1], recompute_ratio[1]), replace(inputs[1]), outputs[1]),
        (Stage(inputs[2], outputs[2], declares[2], calculations[2], recompute_ratio[2]), replace(inputs[2]), outputs[2]),
        (Stage(inputs[3], outputs[3], declares[3], calculations[3], recompute_ratio[3]), replace(inputs[3]), outputs[3]),
        (Stage(inputs[4], outputs[4], declares[4], calculations[4], recompute_ratio[4]), replace(inputs[4]), outputs[4]),
        (Stage(inputs[5], outputs[5], declares[5], calculations[5], recompute_ratio[5]), replace(inputs[5]), outputs[5]),
        (Stage(inputs[6], outputs[6], declares[6], calculations[6], recompute_ratio[6]), replace(inputs[6]), outputs[6]),
        (Stage(inputs[7], outputs[7], declares[7], calculations[7], recompute_ratio[7]), replace(inputs[7]), outputs[7]),
        (criterion, outputs[7], ["loss"])
    ]

def replace(inputs):
    for i in range(len(inputs)):
        if inputs[i] == 'out0':
            inputs[i] = 'input0'
        elif inputs[i] == 'out1':
            inputs[i] = 'input1'
        elif inputs[i] == 'out2':
            inputs[i] = 'input2'
    return inputs

def get_declares():
    return '''self.layer5 = SinusoidalPositionalEmbedding(1024, 1, False, 1026)
self.layer7 = SinusoidalPositionalEmbedding(1024, 1, True, 1026)
self.layer8 = torch.nn.Embedding(33712, 1024, padding_idx=1)
self.layer9 = Scale(1024)
self.layer10 = torch.nn.Embedding(33712, 1024, padding_idx=1)
self.layer11 = Scale(1024)
self.layer13 = torch.nn.Dropout(p=0.1)
self.layer15 = FusedLayerNorm(1024)
self.layer16 = DecoderAttention(1024, 16, dropout=0.1)
self.layer17 = torch.nn.Dropout(p=0.1)
self.layer19 = FusedLayerNorm(1024)
self.layer21 = torch.nn.Dropout(p=0.1)
self.layer23 = FusedLayerNorm(1024)
self.layer24 = EncoderAttention(1024, 16, dropout=0.1, static_kv=False)
self.layer25 = torch.nn.Dropout(p=0.1)
self.layer27 = FusedLayerNorm(1024)
self.layer28 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer29 = torch.nn.Threshold(threshold=0, value=0)
self.layer30 = torch.nn.Dropout(p=0.1)
self.layer31 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer32 = torch.nn.Dropout(p=0.1)
self.layer34 = FusedLayerNorm(1024)
self.layer35 = EncoderAttention(1024, 16, dropout=0.1, static_kv=False)
self.layer36 = torch.nn.Dropout(p=0.1)
self.layer38 = FusedLayerNorm(1024)
self.layer39 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer40 = torch.nn.Threshold(threshold=0, value=0)
self.layer41 = torch.nn.Dropout(p=0.1)
self.layer42 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer43 = torch.nn.Dropout(p=0.1)
self.layer45 = FusedLayerNorm(1024)
self.layer46 = EncoderAttention(1024, 16, dropout=0.1, static_kv=False)
self.layer47 = torch.nn.Dropout(p=0.1)
self.layer49 = FusedLayerNorm(1024)
self.layer50 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer51 = torch.nn.Threshold(threshold=0, value=0)
self.layer52 = torch.nn.Dropout(p=0.1)
self.layer53 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer54 = torch.nn.Dropout(p=0.1)
self.layer56 = FusedLayerNorm(1024)
self.layer57 = EncoderAttention(1024, 16, dropout=0.1, static_kv=False)
self.layer58 = torch.nn.Dropout(p=0.1)
self.layer60 = FusedLayerNorm(1024)
self.layer61 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer62 = torch.nn.Threshold(threshold=0, value=0)
self.layer63 = torch.nn.Dropout(p=0.1)
self.layer64 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer65 = torch.nn.Dropout(p=0.1)
self.layer67 = FusedLayerNorm(1024)
self.layer68 = EncoderAttention(1024, 16, dropout=0.1, static_kv=False)
self.layer69 = torch.nn.Dropout(p=0.1)
self.layer71 = FusedLayerNorm(1024)
self.layer72 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer73 = torch.nn.Threshold(threshold=0, value=0)
self.layer74 = torch.nn.Dropout(p=0.1)
self.layer75 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer76 = torch.nn.Dropout(p=0.1)
self.layer78 = FusedLayerNorm(1024)
self.layer79 = EncoderAttention(1024, 16, dropout=0.1, static_kv=False)
self.layer80 = torch.nn.Dropout(p=0.1)
self.layer82 = FusedLayerNorm(1024)
self.layer83 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer84 = torch.nn.Threshold(threshold=0, value=0)
self.layer85 = torch.nn.Dropout(p=0.1)
self.layer86 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer87 = torch.nn.Dropout(p=0.1)
self.layer89 = FusedLayerNorm(1024)
self.layer90 = EncoderAttention(1024, 16, dropout=0.1, static_kv=False)
self.layer91 = torch.nn.Dropout(p=0.1)
self.layer93 = FusedLayerNorm(1024)
self.layer94 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer95 = torch.nn.Threshold(threshold=0, value=0)
self.layer96 = torch.nn.Dropout(p=0.1)
self.layer97 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer98 = torch.nn.Dropout(p=0.1)
self.layer100 = FusedLayerNorm(1024)
self.layer101 = EncoderAttention(1024, 16, dropout=0.1, static_kv=False)
self.layer102 = torch.nn.Dropout(p=0.1)
self.layer104 = FusedLayerNorm(1024)
self.layer105 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer106 = torch.nn.Threshold(threshold=0, value=0)
self.layer107 = torch.nn.Dropout(p=0.1)
self.layer108 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer109 = torch.nn.Dropout(p=0.1)
self.layer111 = FusedLayerNorm(1024)
self.layer112 = EncoderAttention(1024, 16, dropout=0.1, static_kv=False)
self.layer113 = torch.nn.Dropout(p=0.1)
self.layer115 = FusedLayerNorm(1024)
self.layer116 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer117 = torch.nn.Threshold(threshold=0, value=0)
self.layer118 = torch.nn.Dropout(p=0.1)
self.layer119 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer120 = torch.nn.Dropout(p=0.1)
self.layer122 = FusedLayerNorm(1024)
self.layer123 = EncoderAttention(1024, 16, dropout=0.1, static_kv=False)
self.layer124 = torch.nn.Dropout(p=0.1)
self.layer126 = FusedLayerNorm(1024)
self.layer127 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer128 = torch.nn.Threshold(threshold=0, value=0)
self.layer129 = torch.nn.Dropout(p=0.1)
self.layer130 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer131 = torch.nn.Dropout(p=0.1)
self.layer133 = FusedLayerNorm(1024)
self.layer134 = EncoderAttention(1024, 16, dropout=0.1, static_kv=False)
self.layer135 = torch.nn.Dropout(p=0.1)
self.layer137 = FusedLayerNorm(1024)
self.layer138 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer139 = torch.nn.Threshold(threshold=0, value=0)
self.layer140 = torch.nn.Dropout(p=0.1)
self.layer141 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer142 = torch.nn.Dropout(p=0.1)
self.layer144 = FusedLayerNorm(1024)
self.layer145 = EncoderAttention(1024, 16, dropout=0.1, static_kv=False)
self.layer146 = torch.nn.Dropout(p=0.1)
self.layer148 = FusedLayerNorm(1024)
self.layer149 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer150 = torch.nn.Threshold(threshold=0, value=0)
self.layer151 = torch.nn.Dropout(p=0.1)
self.layer152 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer153 = torch.nn.Dropout(p=0.1)
self.layer155 = FusedLayerNorm(1024)
self.layer156 = EncoderAttention(1024, 16, dropout=0.1, static_kv=True)
self.layer157 = torch.nn.Dropout(p=0.1)
self.layer159 = FusedLayerNorm(1024)
self.layer160 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer161 = torch.nn.Threshold(threshold=0, value=0)
self.layer162 = torch.nn.Dropout(p=0.1)
self.layer163 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer164 = torch.nn.Dropout(p=0.1)
self.layer166 = FusedLayerNorm(1024)
self.layer167 = DecoderAttention(1024, 16, dropout=0.1)
self.layer168 = torch.nn.Dropout(p=0.1)
self.layer170 = FusedLayerNorm(1024)
self.layer171 = EncoderAttention(1024, 16, dropout=0.1, static_kv=True)
self.layer172 = torch.nn.Dropout(p=0.1)
self.layer174 = FusedLayerNorm(1024)
self.layer175 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer176 = torch.nn.Threshold(threshold=0, value=0)
self.layer177 = torch.nn.Dropout(p=0.1)
self.layer178 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer179 = torch.nn.Dropout(p=0.1)
self.layer181 = FusedLayerNorm(1024)
self.layer182 = DecoderAttention(1024, 16, dropout=0.1)
self.layer183 = torch.nn.Dropout(p=0.1)
self.layer185 = FusedLayerNorm(1024)
self.layer186 = EncoderAttention(1024, 16, dropout=0.1, static_kv=True)
self.layer187 = torch.nn.Dropout(p=0.1)
self.layer189 = FusedLayerNorm(1024)
self.layer190 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer191 = torch.nn.Threshold(threshold=0, value=0)
self.layer192 = torch.nn.Dropout(p=0.1)
self.layer193 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer194 = torch.nn.Dropout(p=0.1)
self.layer196 = FusedLayerNorm(1024)
self.layer197 = DecoderAttention(1024, 16, dropout=0.1)
self.layer198 = torch.nn.Dropout(p=0.1)
self.layer200 = FusedLayerNorm(1024)
self.layer201 = EncoderAttention(1024, 16, dropout=0.1, static_kv=True)
self.layer202 = torch.nn.Dropout(p=0.1)
self.layer204 = FusedLayerNorm(1024)
self.layer205 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer206 = torch.nn.Threshold(threshold=0, value=0)
self.layer207 = torch.nn.Dropout(p=0.1)
self.layer208 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer209 = torch.nn.Dropout(p=0.1)
self.layer211 = FusedLayerNorm(1024)
self.layer212 = DecoderAttention(1024, 16, dropout=0.1)
self.layer213 = torch.nn.Dropout(p=0.1)
self.layer215 = FusedLayerNorm(1024)
self.layer216 = EncoderAttention(1024, 16, dropout=0.1, static_kv=True)
self.layer217 = torch.nn.Dropout(p=0.1)
self.layer219 = FusedLayerNorm(1024)
self.layer220 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer221 = torch.nn.Threshold(threshold=0, value=0)
self.layer222 = torch.nn.Dropout(p=0.1)
self.layer223 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer224 = torch.nn.Dropout(p=0.1)
self.layer226 = FusedLayerNorm(1024)
self.layer227 = DecoderAttention(1024, 16, dropout=0.1)
self.layer228 = torch.nn.Dropout(p=0.1)
self.layer230 = FusedLayerNorm(1024)
self.layer231 = EncoderAttention(1024, 16, dropout=0.1, static_kv=True)
self.layer232 = torch.nn.Dropout(p=0.1)
self.layer234 = FusedLayerNorm(1024)
self.layer235 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer236 = torch.nn.Threshold(threshold=0, value=0)
self.layer237 = torch.nn.Dropout(p=0.1)
self.layer238 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer239 = torch.nn.Dropout(p=0.1)
self.layer241 = FusedLayerNorm(1024)
self.layer242 = DecoderAttention(1024, 16, dropout=0.1)
self.layer243 = torch.nn.Dropout(p=0.1)
self.layer245 = FusedLayerNorm(1024)
self.layer246 = EncoderAttention(1024, 16, dropout=0.1, static_kv=True)
self.layer247 = torch.nn.Dropout(p=0.1)
self.layer249 = FusedLayerNorm(1024)
self.layer250 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer251 = torch.nn.Threshold(threshold=0, value=0)
self.layer252 = torch.nn.Dropout(p=0.1)
self.layer253 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer254 = torch.nn.Dropout(p=0.1)
self.layer256 = FusedLayerNorm(1024)
self.layer257 = DecoderAttention(1024, 16, dropout=0.1)
self.layer258 = torch.nn.Dropout(p=0.1)
self.layer260 = FusedLayerNorm(1024)
self.layer261 = EncoderAttention(1024, 16, dropout=0.1, static_kv=True)
self.layer262 = torch.nn.Dropout(p=0.1)
self.layer264 = FusedLayerNorm(1024)
self.layer265 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer266 = torch.nn.Threshold(threshold=0, value=0)
self.layer267 = torch.nn.Dropout(p=0.1)
self.layer268 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer269 = torch.nn.Dropout(p=0.1)
self.layer271 = FusedLayerNorm(1024)
self.layer272 = DecoderAttention(1024, 16, dropout=0.1)
self.layer273 = torch.nn.Dropout(p=0.1)
self.layer275 = FusedLayerNorm(1024)
self.layer276 = EncoderAttention(1024, 16, dropout=0.1, static_kv=True)
self.layer277 = torch.nn.Dropout(p=0.1)
self.layer279 = FusedLayerNorm(1024)
self.layer280 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer281 = torch.nn.Threshold(threshold=0, value=0)
self.layer282 = torch.nn.Dropout(p=0.1)
self.layer283 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer284 = torch.nn.Dropout(p=0.1)
self.layer286 = FusedLayerNorm(1024)
self.layer287 = DecoderAttention(1024, 16, dropout=0.1)
self.layer288 = torch.nn.Dropout(p=0.1)
self.layer290 = FusedLayerNorm(1024)
self.layer291 = EncoderAttention(1024, 16, dropout=0.1, static_kv=True)
self.layer292 = torch.nn.Dropout(p=0.1)
self.layer294 = FusedLayerNorm(1024)
self.layer295 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer296 = torch.nn.Threshold(threshold=0, value=0)
self.layer297 = torch.nn.Dropout(p=0.1)
self.layer298 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer299 = torch.nn.Dropout(p=0.1)
self.layer301 = FusedLayerNorm(1024)
self.layer302 = DecoderAttention(1024, 16, dropout=0.1)
self.layer303 = torch.nn.Dropout(p=0.1)
self.layer305 = FusedLayerNorm(1024)
self.layer306 = EncoderAttention(1024, 16, dropout=0.1, static_kv=True)
self.layer307 = torch.nn.Dropout(p=0.1)
self.layer309 = FusedLayerNorm(1024)
self.layer310 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer311 = torch.nn.Threshold(threshold=0, value=0)
self.layer312 = torch.nn.Dropout(p=0.1)
self.layer313 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer314 = torch.nn.Dropout(p=0.1)
self.layer316 = FusedLayerNorm(1024)
self.layer317 = DecoderAttention(1024, 16, dropout=0.1)
self.layer318 = torch.nn.Dropout(p=0.1)
self.layer320 = FusedLayerNorm(1024)
self.layer321 = EncoderAttention(1024, 16, dropout=0.1, static_kv=True)
self.layer322 = torch.nn.Dropout(p=0.1)
self.layer324 = FusedLayerNorm(1024)
self.layer325 = torch.nn.Linear(in_features=1024, out_features=4096, bias=True)
self.layer326 = torch.nn.Threshold(threshold=0, value=0)
self.layer327 = torch.nn.Dropout(p=0.1)
self.layer328 = torch.nn.Linear(in_features=4096, out_features=1024, bias=True)
self.layer329 = torch.nn.Dropout(p=0.1)
self.layer331 = FusedLayerNorm(1024)
self.layer333 = torch.nn.Linear(in_features=1024, out_features=33712, bias=False)'''

def get_caculations():
    return '''out7 = self.layer7(out0)
out10 = self.layer10(out0)
out11 = self.layer11(out10)
out11 = out11 + out7
out21 = self.layer21(out11)
out22 = out21.transpose(0, 1)
out23 = self.layer23(out22)
out24 = self.layer24(out23, out23, out1)
out25 = self.layer25(out24)
out25 = out25 + out22
out27 = self.layer27(out25)
out28 = self.layer28(out27)
out29 = self.layer29(out28)
out30 = self.layer30(out29)
out31 = self.layer31(out30)
out32 = self.layer32(out31)
out32 = out32 + out25
out34 = self.layer34(out32)
out35 = self.layer35(out34, out34, out1)
out36 = self.layer36(out35)
out36 = out36 + out32
out38 = self.layer38(out36)
out39 = self.layer39(out38)
out40 = self.layer40(out39)
out41 = self.layer41(out40)
out42 = self.layer42(out41)
out43 = self.layer43(out42)
out43 = out43 + out36
out45 = self.layer45(out43)
out46 = self.layer46(out45, out45, out1)
out47 = self.layer47(out46)
out47 = out47 + out43
out49 = self.layer49(out47)
out50 = self.layer50(out49)
out51 = self.layer51(out50)
out52 = self.layer52(out51)
out53 = self.layer53(out52)
out54 = self.layer54(out53)
out54 = out54 + out47
out56 = self.layer56(out54)
out57 = self.layer57(out56, out56, out1)
out58 = self.layer58(out57)
out58 = out58 + out54
out60 = self.layer60(out58)
out61 = self.layer61(out60)
out62 = self.layer62(out61)
out63 = self.layer63(out62)
out64 = self.layer64(out63)
out65 = self.layer65(out64)
out65 = out65 + out58
out67 = self.layer67(out65)
out68 = self.layer68(out67, out67, out1)
out69 = self.layer69(out68)
out69 = out69 + out65
out71 = self.layer71(out69)
out72 = self.layer72(out71)
out73 = self.layer73(out72)
out74 = self.layer74(out73)
out75 = self.layer75(out74)
out76 = self.layer76(out75)
out76 = out76 + out69
out78 = self.layer78(out76)
out79 = self.layer79(out78, out78, out1)
out80 = self.layer80(out79)
out80 = out80 + out76
out82 = self.layer82(out80)
out83 = self.layer83(out82)
out84 = self.layer84(out83)
out85 = self.layer85(out84)
out86 = self.layer86(out85)
out87 = self.layer87(out86)
out87 = out87 + out80
out89 = self.layer89(out87)
out90 = self.layer90(out89, out89, out1)
out91 = self.layer91(out90)
out91 = out91 + out87
out93 = self.layer93(out91)
out94 = self.layer94(out93)
out95 = self.layer95(out94)
out96 = self.layer96(out95)
out97 = self.layer97(out96)
out98 = self.layer98(out97)
out98 = out98 + out91
out100 = self.layer100(out98)
out101 = self.layer101(out100, out100, out1)
out102 = self.layer102(out101)
out102 = out102 + out98
out104 = self.layer104(out102)
out105 = self.layer105(out104)
out106 = self.layer106(out105)
out107 = self.layer107(out106)
out108 = self.layer108(out107)
out109 = self.layer109(out108)
out109 = out109 + out102
out111 = self.layer111(out109)
out112 = self.layer112(out111, out111, out1)
out113 = self.layer113(out112)
out113 = out113 + out109
out115 = self.layer115(out113)
out116 = self.layer116(out115)
out117 = self.layer117(out116)
out118 = self.layer118(out117)
out119 = self.layer119(out118)
out120 = self.layer120(out119)
out120 = out120 + out113
out122 = self.layer122(out120)
out123 = self.layer123(out122, out122, out1)
out124 = self.layer124(out123)
out124 = out124 + out120
out126 = self.layer126(out124)
out127 = self.layer127(out126)
out128 = self.layer128(out127)
out129 = self.layer129(out128)
out130 = self.layer130(out129)
out131 = self.layer131(out130)
out131 = out131 + out124
out133 = self.layer133(out131)
out134 = self.layer134(out133, out133, out1)
out135 = self.layer135(out134)
out135 = out135 + out131
out137 = self.layer137(out135)
out138 = self.layer138(out137)
out139 = self.layer139(out138)
out140 = self.layer140(out139)
out141 = self.layer141(out140)
out142 = self.layer142(out141)
out142 = out142 + out135
out144 = self.layer144(out142)
out145 = self.layer145(out144, out144, out1)
out146 = self.layer146(out145)
out146 = out146 + out142
out148 = self.layer148(out146)
out149 = self.layer149(out148)
out150 = self.layer150(out149)
out151 = self.layer151(out150)
out152 = self.layer152(out151)
out153 = self.layer153(out152)
out153 = out153 + out146
out5 = self.layer5(out2)
out8 = self.layer8(out2)
out9 = self.layer9(out8)
out9 = out9 + out5
out13 = self.layer13(out9)
out14 = out13.transpose(0, 1)
out15 = self.layer15(out14)
out16 = self.layer16(out15)
out17 = self.layer17(out16)
out17 = out17 + out14
out19 = self.layer19(out17)
out155 = self.layer155(out153)
out156 = self.layer156(out19, out155, out1)
out157 = self.layer157(out156)
out157 = out157 + out17
out159 = self.layer159(out157)
out160 = self.layer160(out159)
out161 = self.layer161(out160)
out162 = self.layer162(out161)
out163 = self.layer163(out162)
out164 = self.layer164(out163)
out164 = out164 + out157
out166 = self.layer166(out164)
out167 = self.layer167(out166)
out168 = self.layer168(out167)
out168 = out168 + out164
out170 = self.layer170(out168)
out171 = self.layer171(out170, out155, out1)
out172 = self.layer172(out171)
out172 = out172 + out168
out174 = self.layer174(out172)
out175 = self.layer175(out174)
out176 = self.layer176(out175)
out177 = self.layer177(out176)
out178 = self.layer178(out177)
out179 = self.layer179(out178)
out179 = out179 + out172
out181 = self.layer181(out179)
out182 = self.layer182(out181)
out183 = self.layer183(out182)
out183 = out183 + out179
out185 = self.layer185(out183)
out186 = self.layer186(out185, out155, out1)
out187 = self.layer187(out186)
out187 = out187 + out183
out189 = self.layer189(out187)
out190 = self.layer190(out189)
out191 = self.layer191(out190)
out192 = self.layer192(out191)
out193 = self.layer193(out192)
out194 = self.layer194(out193)
out194 = out194 + out187
out196 = self.layer196(out194)
out197 = self.layer197(out196)
out198 = self.layer198(out197)
out198 = out198 + out194
out200 = self.layer200(out198)
out201 = self.layer201(out200, out155, out1)
out202 = self.layer202(out201)
out202 = out202 + out198
out204 = self.layer204(out202)
out205 = self.layer205(out204)
out206 = self.layer206(out205)
out207 = self.layer207(out206)
out208 = self.layer208(out207)
out209 = self.layer209(out208)
out209 = out209 + out202
out211 = self.layer211(out209)
out212 = self.layer212(out211)
out213 = self.layer213(out212)
out213 = out213 + out209
out215 = self.layer215(out213)
out216 = self.layer216(out215, out155, out1)
out217 = self.layer217(out216)
out217 = out217 + out213
out219 = self.layer219(out217)
out220 = self.layer220(out219)
out221 = self.layer221(out220)
out222 = self.layer222(out221)
out223 = self.layer223(out222)
out224 = self.layer224(out223)
out224 = out224 + out217
out226 = self.layer226(out224)
out227 = self.layer227(out226)
out228 = self.layer228(out227)
out228 = out228 + out224
out230 = self.layer230(out228)
out231 = self.layer231(out230, out155, out1)
out232 = self.layer232(out231)
out232 = out232 + out228
out234 = self.layer234(out232)
out235 = self.layer235(out234)
out236 = self.layer236(out235)
out237 = self.layer237(out236)
out238 = self.layer238(out237)
out239 = self.layer239(out238)
out239 = out239 + out232
out241 = self.layer241(out239)
out242 = self.layer242(out241)
out243 = self.layer243(out242)
out243 = out243 + out239
out245 = self.layer245(out243)
out246 = self.layer246(out245, out155, out1)
out247 = self.layer247(out246)
out247 = out247 + out243
out249 = self.layer249(out247)
out250 = self.layer250(out249)
out251 = self.layer251(out250)
out252 = self.layer252(out251)
out253 = self.layer253(out252)
out254 = self.layer254(out253)
out254 = out254 + out247
out256 = self.layer256(out254)
out257 = self.layer257(out256)
out258 = self.layer258(out257)
out258 = out258 + out254
out260 = self.layer260(out258)
out261 = self.layer261(out260, out155, out1)
out262 = self.layer262(out261)
out262 = out262 + out258
out264 = self.layer264(out262)
out265 = self.layer265(out264)
out266 = self.layer266(out265)
out267 = self.layer267(out266)
out268 = self.layer268(out267)
out269 = self.layer269(out268)
out269 = out269 + out262
out271 = self.layer271(out269)
out272 = self.layer272(out271)
out273 = self.layer273(out272)
out273 = out273 + out269
out275 = self.layer275(out273)
out276 = self.layer276(out275, out155, out1)
out277 = self.layer277(out276)
out277 = out277 + out273
out279 = self.layer279(out277)
out280 = self.layer280(out279)
out281 = self.layer281(out280)
out282 = self.layer282(out281)
out283 = self.layer283(out282)
out284 = self.layer284(out283)
out284 = out284 + out277
out286 = self.layer286(out284)
out287 = self.layer287(out286)
out288 = self.layer288(out287)
out288 = out288 + out284
out290 = self.layer290(out288)
out291 = self.layer291(out290, out155, out1)
out292 = self.layer292(out291)
out292 = out292 + out288
out294 = self.layer294(out292)
out295 = self.layer295(out294)
out296 = self.layer296(out295)
out297 = self.layer297(out296)
out298 = self.layer298(out297)
out299 = self.layer299(out298)
out299 = out299 + out292
out301 = self.layer301(out299)
out302 = self.layer302(out301)
out303 = self.layer303(out302)
out303 = out303 + out299
out305 = self.layer305(out303)
out306 = self.layer306(out305, out155, out1)
out307 = self.layer307(out306)
out307 = out307 + out303
out309 = self.layer309(out307)
out310 = self.layer310(out309)
out311 = self.layer311(out310)
out312 = self.layer312(out311)
out313 = self.layer313(out312)
out314 = self.layer314(out313)
out314 = out314 + out307
out316 = self.layer316(out314)
out317 = self.layer317(out316)
out318 = self.layer318(out317)
out318 = out318 + out314
out320 = self.layer320(out318)
out321 = self.layer321(out320, out155, out1)
out322 = self.layer322(out321)
out322 = out322 + out318
out324 = self.layer324(out322)
out325 = self.layer325(out324)
out326 = self.layer326(out325)
out327 = self.layer327(out326)
out328 = self.layer328(out327)
out329 = self.layer329(out328)
out329 = out329 + out322
out331 = self.layer331(out329)
out332 = out331.transpose(0, 1)
out333 = self.layer333(out332)'''