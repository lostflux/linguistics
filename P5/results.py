"""
================================================================================
                                      Opts                                      
--------------------------------------------------------------------------------
                                   cuda: 0                                      
                                nepochs: 100                                    
                         checkpoint_dir: checkpoints                            
                          learning_rate: 0.005                                  
                               lr_decay: 0.99                                   
                             batch_size: 64                                     
                            hidden_size: 20                                     
                           decoder_type: transformer                            
                 num_transformer_layers: 3                                      
================================================================================
================================================================================
                                   Data Stats                                   
--------------------------------------------------------------------------------
('invited', 'invitedway')
('absolute', 'absoluteway')
('sad', 'adsay')
('tolerably', 'olerablytay')
('calculation', 'alculationcay')
Num unique word pairs: 6387
Vocabulary: dict_keys(['-', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'SOS', 'EOS'])
Vocab size: 29
================================================================================
Epoch:   1 | Train loss: 1.982 | Val loss: 1.977 | Gen: thththththththththth adawaydaydaydaydayda onday waywlwlwlwlwlwlwlwlw --------------------
Epoch:   2 | Train loss: 1.371 | Val loss: 1.801 | Gen: thththththththththth aaawrawawraawawawraw itnnnncititititititi isisisisisisisisisis --------------------
Epoch:   3 | Train loss: 1.041 | Val loss: 1.572 | Gen: etay awrway ongway-itititititida isisisisisisisisisis oringway
Epoch:   4 | Train loss: 0.842 | Val loss: 1.338 | Gen: ethththay aairway ongway-itingway isisisisisisisisisis orfingway
Epoch:   5 | Train loss: 0.678 | Val loss: 1.114 | Gen: etththththay airay ongway-itingngngway isway orkingway
Epoch:   6 | Train loss: 0.552 | Val loss: 1.165 | Gen: eththay airway ondcondindiondiondin isisisasisasisway orkingway
Epoch:   7 | Train loss: 0.478 | Val loss: 1.022 | Gen: eththay airway ondititingway isisisway orkingway
Epoch:   8 | Train loss: 0.476 | Val loss: 1.084 | Gen: eththty airway-ay onitinindioninininin isisisiswasway orfayiningway
Epoch:   9 | Train loss: 0.438 | Val loss: 0.834 | Gen: ethay away ondiongcay isay orkingway
Epoch:  10 | Train loss: 0.328 | Val loss: 1.010 | Gen: ethehay airway ondcay isway orwayrwinplingway
Epoch:  11 | Train loss: 0.324 | Val loss: 0.803 | Gen: ethay airway ondinioniongcay isway orkingway
Epoch:  12 | Train loss: 0.293 | Val loss: 0.840 | Gen: ethay airway ondionionioniongcay asway orkay
Epoch:  13 | Train loss: 0.280 | Val loss: 0.902 | Gen: eethay airway onindisininisingwayi isisisy eorkingway
Epoch:  14 | Train loss: 0.302 | Val loss: 0.827 | Gen: ethay airway ondiyitingway isway orkingway
Epoch:  15 | Train loss: 0.224 | Val loss: 0.647 | Gen: ethay airway onditionrcay isway orkingway
Epoch:  16 | Train loss: 0.201 | Val loss: 0.767 | Gen: ethay airwayay ondinditionionionion isway orkingway
Epoch:  17 | Train loss: 0.188 | Val loss: 0.588 | Gen: ethay airway ondiy-ingcaninininin isway orkingway
Epoch:  18 | Train loss: 0.186 | Val loss: 0.665 | Gen: ehay airway ondquongway isway erkway
Epoch:  19 | Train loss: 0.193 | Val loss: 0.773 | Gen: ethay airway uondioningcay isway orkingway
Epoch:  20 | Train loss: 0.199 | Val loss: 0.797 | Gen: ethehay arway ondioningcay isway orkingway
Epoch:  21 | Train loss: 0.210 | Val loss: 0.499 | Gen: ethay airway onditiongfay isway orkingway
Epoch:  22 | Train loss: 0.151 | Val loss: 0.529 | Gen: ethay airway onditingnay isway orkingway
Epoch:  23 | Train loss: 0.123 | Val loss: 0.421 | Gen: ethay airway onditionionionionion isway orkingway
Epoch:  24 | Train loss: 0.129 | Val loss: 0.384 | Gen: ethay airway ondiningcay isway orkarkngway
Epoch:  25 | Train loss: 0.107 | Val loss: 0.352 | Gen: ethay airway onditininingcay isway orkingway
Epoch:  26 | Train loss: 0.077 | Val loss: 0.331 | Gen: ethay airway onditiniongcay isway orkingway
Epoch:  27 | Train loss: 0.076 | Val loss: 0.545 | Gen: ethay airway onditionitionioninio isway orkarkingway
Epoch:  28 | Train loss: 0.115 | Val loss: 0.408 | Gen: ethay arway ondisingcay isway orkayway
Epoch:  29 | Train loss: 0.103 | Val loss: 0.283 | Gen: ethay airway onditiongcay isway orkaygway
Epoch:  30 | Train loss: 0.088 | Val loss: 0.714 | Gen: ethay airway onditingfay isway orkingway
Epoch:  31 | Train loss: 0.148 | Val loss: 0.530 | Gen: ethay airway onditioningcay isway orkay
Epoch:  32 | Train loss: 0.089 | Val loss: 0.213 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  33 | Train loss: 0.060 | Val loss: 0.273 | Gen: ethay airway onditingcay isway orkingway
Epoch:  34 | Train loss: 0.047 | Val loss: 0.236 | Gen: ethay airway onditioningcay isway orkingway
Epoch:  35 | Train loss: 0.043 | Val loss: 0.251 | Gen: ethay airway ondinditiningcay isway orkingway
Epoch:  36 | Train loss: 0.051 | Val loss: 0.391 | Gen: ethay airway onditiongcay isway orkingway
Epoch:  37 | Train loss: 0.046 | Val loss: 0.209 | Gen: ethay airway onditingcay isway orkingway
Epoch:  38 | Train loss: 0.093 | Val loss: 1.049 | Gen: ethay airway onndcay isway ongway
Epoch:  39 | Train loss: 0.258 | Val loss: 0.990 | Gen: ethay arway oncay isway orywongway
Epoch:  40 | Train loss: 0.212 | Val loss: 0.423 | Gen: ethay airway ondiongcay isway orkingway
Epoch:  41 | Train loss: 0.098 | Val loss: 0.271 | Gen: ethay airway onditininiongcay isway orkingway
Epoch:  42 | Train loss: 0.081 | Val loss: 0.289 | Gen: ethay airway onditingcay isway orkay
Epoch:  43 | Train loss: 0.052 | Val loss: 0.211 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  44 | Train loss: 0.049 | Val loss: 0.209 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  45 | Train loss: 0.033 | Val loss: 0.187 | Gen: ethay airway onditinioningcay isway orkingway
Epoch:  46 | Train loss: 0.040 | Val loss: 0.341 | Gen: ethay airway onditisiningcay isway orkingway
Epoch:  47 | Train loss: 0.068 | Val loss: 0.240 | Gen: ethay airway onditingcay isway orkingway
Epoch:  48 | Train loss: 0.049 | Val loss: 0.627 | Gen: ethay airway onditiongcay isway orkay
Epoch:  49 | Train loss: 0.090 | Val loss: 0.373 | Gen: ethay airway onditinininingpay isway orkirkingway
Epoch:  50 | Train loss: 0.083 | Val loss: 0.265 | Gen: ethay airway onditioniningcay isway orkingway
Epoch:  51 | Train loss: 0.046 | Val loss: 0.143 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  52 | Train loss: 0.033 | Val loss: 0.219 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  53 | Train loss: 0.029 | Val loss: 0.117 | Gen: ethay airway onditioniningcay isway orkingway
Epoch:  54 | Train loss: 0.020 | Val loss: 0.166 | Gen: ethay airway onditingcay isway orkingway
Epoch:  55 | Train loss: 0.020 | Val loss: 0.099 | Gen: ethay airway onditionisioningcay isway orkingway
Epoch:  56 | Train loss: 0.028 | Val loss: 0.643 | Gen: ethay airway onditiningnionrnrnio isway orkway
Epoch:  57 | Train loss: 0.086 | Val loss: 0.194 | Gen: ethay airway onditisioningcay isway orkingway
Epoch:  58 | Train loss: 0.056 | Val loss: 0.242 | Gen: ethay airway onditingcay isway orkingway
Epoch:  59 | Train loss: 0.054 | Val loss: 0.177 | Gen: ethay airway onditingcay isway orkingway
Epoch:  60 | Train loss: 0.034 | Val loss: 0.142 | Gen: ethay airway onditioningcay isway orkingway
Epoch:  61 | Train loss: 0.018 | Val loss: 0.119 | Gen: ethay airway onditioningcay isway orkingway
Epoch:  62 | Train loss: 0.012 | Val loss: 0.103 | Gen: ethay airway onditioningcay isway orkingway
Epoch:  63 | Train loss: 0.009 | Val loss: 0.074 | Gen: ethay airway onditioningcay isway orkingway
Epoch:  64 | Train loss: 0.029 | Val loss: 0.269 | Gen: ethay airway onditioningcay isway orkingway
Epoch:  65 | Train loss: 0.044 | Val loss: 0.364 | Gen: ethay airway onditinioniningcay isway orkingway
Epoch:  66 | Train loss: 0.038 | Val loss: 0.406 | Gen: ethay airway ondisay isway orkingway
Epoch:  67 | Train loss: 0.028 | Val loss: 0.149 | Gen: ethay airway onditiongcay isway orkingway
Epoch:  68 | Train loss: 0.036 | Val loss: 0.248 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  69 | Train loss: 0.041 | Val loss: 0.264 | Gen: ethay airway onditingcay isway orkingway
Epoch:  70 | Train loss: 0.051 | Val loss: 0.229 | Gen: ethay airway onditinioningcay isway orkingway
Epoch:  71 | Train loss: 0.031 | Val loss: 0.262 | Gen: ethay airway onditiongnay isway orkingway
Epoch:  72 | Train loss: 0.061 | Val loss: 0.238 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  73 | Train loss: 0.049 | Val loss: 0.187 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  74 | Train loss: 0.037 | Val loss: 0.130 | Gen: ethay airway ondioningcay isway orkingway
Epoch:  75 | Train loss: 0.028 | Val loss: 0.183 | Gen: ethay airway onditiongcay isway orkingway
Epoch:  76 | Train loss: 0.050 | Val loss: 0.305 | Gen: ethay airway ondieingcay isway orkingway
Epoch:  77 | Train loss: 0.068 | Val loss: 0.280 | Gen: ethay airway ondisioningway isway orkingway
Epoch:  78 | Train loss: 0.057 | Val loss: 0.227 | Gen: ethay airway ondititiningcay isway orkingway
Epoch:  79 | Train loss: 0.036 | Val loss: 0.161 | Gen: ethay airway onditingcay isway orkingway
Epoch:  80 | Train loss: 0.018 | Val loss: 0.142 | Gen: ethay airway onditioningcay isway orkingway
Epoch:  81 | Train loss: 0.012 | Val loss: 0.095 | Gen: ethay airway onditingcay isway orkingway
Epoch:  82 | Train loss: 0.006 | Val loss: 0.098 | Gen: ethay airway onditingcay isway orkingway
Epoch:  83 | Train loss: 0.005 | Val loss: 0.092 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  84 | Train loss: 0.007 | Val loss: 0.150 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  85 | Train loss: 0.021 | Val loss: 0.141 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  86 | Train loss: 0.013 | Val loss: 0.081 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  87 | Train loss: 0.006 | Val loss: 0.088 | Gen: ethay airway onditingcay isway orkingway
Epoch:  88 | Train loss: 0.004 | Val loss: 0.082 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  89 | Train loss: 0.006 | Val loss: 0.091 | Gen: ethay airway onditingcay isway orkingway
Epoch:  90 | Train loss: 0.003 | Val loss: 0.082 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  91 | Train loss: 0.003 | Val loss: 0.083 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  92 | Train loss: 0.002 | Val loss: 0.086 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  93 | Train loss: 0.002 | Val loss: 0.077 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  94 | Train loss: 0.002 | Val loss: 0.104 | Gen: ethay airway onditiningcay isway orkingway
Epoch:  95 | Train loss: 0.009 | Val loss: 0.119 | Gen: ethay airway onditingcay isway orkingway
Epoch:  96 | Train loss: 0.028 | Val loss: 1.268 | Gen: ethay airway onditiondgway issway orkingway
Epoch:  97 | Train loss: 0.092 | Val loss: 0.256 | Gen: ethay airway onditingcay isway orkingway
Epoch:  98 | Train loss: 0.028 | Val loss: 0.112 | Gen: ethay airway onditioningcay isway orkingway
Epoch:  99 | Train loss: 0.013 | Val loss: 0.110 | Gen: ethay airway onditioningcay isway orkingway
Epoch: 100 | Train loss: 0.005 | Val loss: 0.101 | Gen: ethay airway onditioningcay isway orkingway
source:         the air conditioning is working
translated:     ethay airway onditioningcay isway orkingway
"""
