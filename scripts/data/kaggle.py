# Credit card data from European provider: https://www.kaggle.com/mlg-ulb/creditcardfraud/home

# histogram fractions for transaction amount 
amount_dist = [0.24301720112216343, 0.11091370647491108, 0.0810935124487811, 0.05606252655306927, 0.03932487614419589, 0.038727980702721494, 0.03223586498927344, 0.025069608541924884, 0.024683382079794387, 0.022906740353994107, 0.018904029746459883, 0.0164637807357263, 0.013991931378091129, 0.013570593419403315, 0.012935075331715864, 0.0129280530324044, 0.012836763141355375, 0.012078354815717311, 0.00944850372357421, 0.007615683603282223, 0.0073172358825450215, 0.00693803171972599, 0.006934520570070258, 0.006281446734104148, 0.006162067645809267, 0.005856597625760603, 0.005835530727826212, 0.005252679884974737, 0.0052175683884174194, 0.005098189300122539, 0.004834853075942656, 0.004789208130418143, 0.0038376865737148316, 0.003686707138518365, 0.0036621290909282424, 0.003560305750912021, 0.0033145252750107967, 0.003156523540502867, 0.0027211409831921266, 0.0026965629356020043, 0.0024121598134877304, 0.0023314033714058996, 0.0022646915279469957, 0.0022506469293240685, 0.0022155354327667506, 0.002159357038275042, 0.002117223242406261, 0.002022422201701503, 0.0018398424196034507, 0.0018117532223575965, 0.0017450413788986927, 0.0016888629844069843, 0.0016502403381939347, 0.001551928147833445, 0.0015484169981777134, 0.0015484169981777134, 0.0015449058485219815, 0.0015449058485219815, 0.0014220156105713693, 0.0013869041140140517, 0.0013061476719322207, 0.0012464581277847806, 0.0012324135291618536, 0.00122539122985039, 0.0011657016857029498, 0.0011060121415555095, 0.0010603671960309963, 0.0010287668491294104, 0.0010041888015392881, 0.0010006776518835562, 0.0009971665022278245, 0.0009515215567033114, 0.0008707651146214805, 0.000863742815310017, 0.0008426759173756263, 0.0008286313187526992, 0.0007268079787364777, 0.0007268079787364777, 0.0006916964821791599, 0.0006881853325234282, 0.0006776518835562328, 0.0006776518835562328, 0.0006706295842447693, 0.0006530738359661104, 0.0006179623394087926, 0.0005793396931957431, 0.0005758285435400113, 0.0005688062442285478, 0.000565295094572816, 0.0005512504959498889, 0.0005407170469826936, 0.0005161389993925711, 0.0005091167000811076, 0.0004950721014581804, 0.0004669829042123262, 0.00045996060490086267, 0.0004424048566222038, 0.0004424048566222038, 0.0004424048566222038, 0.00043538255731074025, 0.0004283602579992767, 0.00042484910834354495, 0.00042484910834354495, 0.0004143156593763496, 0.00040729336006488603, 0.00040729336006488603, 0.0004002710607534225, 0.0003932487614419589, 0.0003897376117862272, 0.00038622646213049537, 0.0003792041628190318, 0.00037218186350756826, 0.00037218186350756826, 0.0003581372648846412, 0.0003581372648846412, 0.0003546261152289094, 0.00035111496557317765, 0.00034760381591744584, 0.00033707036695025054, 0.00030195887039293276, 0.00029844772073720096, 0.00029142542142573746, 0.00029142542142573746, 0.00029142542142573746, 0.00028791427177000565, 0.00028791427177000565, 0.00028791427177000565, 0.0002844031221142739, 0.00026333622417988324, 0.00026333622417988324, 0.00025982507452415143, 0.0002563139248684197, 0.0002563139248684197, 0.00023173587727829724, 0.00023173587727829724, 0.0002212024283111019, 0.0002212024283111019, 0.0002212024283111019, 0.0002212024283111019, 0.00021066897934390657, 0.00020364668003244302, 0.00019662438072097946, 0.00019662438072097946, 0.00019662438072097946, 0.00019662438072097946, 0.0001896020814095159, 0.0001896020814095159, 0.0001896020814095159, 0.00017555748278658882, 0.00017555748278658882, 0.00017555748278658882, 0.00017555748278658882, 0.00017204633313085705, 0.00017204633313085705, 0.00017204633313085705, 0.0001650240338193935, 0.0001615128841636617, 0.00015800173450792994, 0.00015449058485219816, 0.00015449058485219816, 0.00015449058485219816, 0.00015449058485219816, 0.0001474682855407346, 0.00014044598622927105, 0.00014044598622927105, 0.00013693483657353927, 0.00013693483657353927, 0.00013693483657353927, 0.0001334236869178075, 0.0001334236869178075, 0.00012991253726207572, 0.00012991253726207572, 0.00012640138760634394, 0.0001193790882948804, 0.0001193790882948804, 0.0001193790882948804, 0.00011586793863914862, 0.00011235678898341684, 0.00011235678898341684, 0.00011235678898341684, 0.00010884563932768506, 0.00010884563932768506, 0.00010884563932768506, 0.00010533448967195329, 0.00010182334001622151, 0.00010182334001622151, 0.00010182334001622151, 9.831219036048973e-05, 9.831219036048973e-05, 9.480104070475795e-05, 9.128989104902619e-05, 9.128989104902619e-05, 9.128989104902619e-05, 9.128989104902619e-05, 8.777874139329441e-05, 8.777874139329441e-05, 8.777874139329441e-05, 8.777874139329441e-05, 8.777874139329441e-05, 8.777874139329441e-05, 8.777874139329441e-05, 8.777874139329441e-05, 8.777874139329441e-05, 8.426759173756263e-05, 8.075644208183086e-05, 8.075644208183086e-05, 8.075644208183086e-05, 8.075644208183086e-05, 7.724529242609908e-05, 7.724529242609908e-05, 7.724529242609908e-05, 7.724529242609908e-05, 7.724529242609908e-05, 7.724529242609908e-05, 7.37341427703673e-05, 7.37341427703673e-05, 7.37341427703673e-05, 7.37341427703673e-05, 7.022299311463552e-05, 7.022299311463552e-05, 7.022299311463552e-05, 7.022299311463552e-05, 7.022299311463552e-05, 7.022299311463552e-05, 6.671184345890375e-05, 6.671184345890375e-05, 6.671184345890375e-05, 6.671184345890375e-05, 6.671184345890375e-05, 6.671184345890375e-05, 6.671184345890375e-05, 6.671184345890375e-05, 6.671184345890375e-05, 6.671184345890375e-05, 6.320069380317197e-05, 6.320069380317197e-05, 6.320069380317197e-05, 6.320069380317197e-05, 5.96895441474402e-05, 5.96895441474402e-05, 5.96895441474402e-05, 5.96895441474402e-05, 5.96895441474402e-05, 5.96895441474402e-05, 5.96895441474402e-05, 5.96895441474402e-05, 5.96895441474402e-05, 5.617839449170842e-05, 5.617839449170842e-05, 5.617839449170842e-05, 5.617839449170842e-05, 5.266724483597664e-05, 5.266724483597664e-05, 5.266724483597664e-05, 4.9156095180244865e-05, 4.9156095180244865e-05, 4.9156095180244865e-05, 4.9156095180244865e-05, 4.9156095180244865e-05, 4.9156095180244865e-05, 4.9156095180244865e-05, 4.9156095180244865e-05, 4.5644945524513095e-05, 4.5644945524513095e-05, 4.5644945524513095e-05, 4.5644945524513095e-05, 4.5644945524513095e-05, 4.213379586878132e-05, 4.213379586878132e-05, 4.213379586878132e-05, 4.213379586878132e-05, 4.213379586878132e-05, 4.213379586878132e-05, 3.862264621304954e-05, 3.862264621304954e-05, 3.862264621304954e-05, 3.862264621304954e-05, 3.862264621304954e-05, 3.862264621304954e-05, 3.511149655731776e-05, 3.511149655731776e-05, 3.511149655731776e-05, 3.511149655731776e-05, 3.511149655731776e-05, 3.511149655731776e-05, 3.511149655731776e-05, 3.1600346901585984e-05, 3.1600346901585984e-05, 3.1600346901585984e-05, 3.1600346901585984e-05, 3.1600346901585984e-05, 3.1600346901585984e-05, 3.1600346901585984e-05, 3.1600346901585984e-05, 3.1600346901585984e-05, 3.1600346901585984e-05, 3.1600346901585984e-05, 3.1600346901585984e-05, 3.1600346901585984e-05, 3.1600346901585984e-05, 3.1600346901585984e-05, 3.1600346901585984e-05, 2.808919724585421e-05, 2.808919724585421e-05, 2.808919724585421e-05, 2.808919724585421e-05, 2.808919724585421e-05, 2.808919724585421e-05, 2.808919724585421e-05, 2.808919724585421e-05, 2.808919724585421e-05, 2.808919724585421e-05, 2.808919724585421e-05, 2.808919724585421e-05, 2.808919724585421e-05, 2.808919724585421e-05, 2.808919724585421e-05, 2.808919724585421e-05, 2.4578047590122433e-05, 2.4578047590122433e-05, 2.4578047590122433e-05, 2.4578047590122433e-05, 2.4578047590122433e-05, 2.4578047590122433e-05, 2.4578047590122433e-05, 2.4578047590122433e-05, 2.4578047590122433e-05, 2.4578047590122433e-05, 2.4578047590122433e-05, 2.4578047590122433e-05, 2.4578047590122433e-05, 2.4578047590122433e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 2.106689793439066e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.755574827865888e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.4044598622927105e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 1.053344896719533e-05, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 7.0222993114635526e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06, 3.5111496557317763e-06]

# histogram bins for transaction amount
amount_bins = [5.138, 10.276, 15.415, 20.553, 25.691, 30.829, 35.968, 41.106, 46.244, 51.382, 56.521, 61.659, 66.797, 71.935, 77.073, 82.212, 87.35, 92.488, 97.626, 102.765, 107.903, 113.041, 118.179, 123.318, 128.456, 133.594, 138.732, 143.87, 149.009, 154.147, 159.285, 164.423, 169.562, 174.7, 179.838, 184.976, 190.115, 195.253, 200.391, 205.529, 210.668, 215.806, 220.944, 226.082, 231.22, 236.359, 241.497, 246.635, 251.773, 256.912, 262.05, 267.188, 272.326, 277.465, 282.603, 287.741, 292.879, 298.017, 303.156, 308.294, 313.432, 318.57, 323.709, 328.847, 333.985, 339.123, 344.262, 349.4, 354.538, 359.676, 364.814, 369.953, 375.091, 380.229, 385.367, 390.506, 395.644, 400.782, 405.92, 411.059, 416.197, 421.335, 426.473, 431.611, 436.75, 441.888, 447.026, 452.164, 457.303, 462.441, 467.579, 472.717, 477.856, 482.994, 488.132, 493.27, 498.409, 503.547, 508.685, 513.823, 518.961, 524.1, 529.238, 534.376, 539.514, 544.653, 549.791, 554.929, 560.067, 565.206, 570.344, 575.482, 580.62, 585.758, 590.897, 596.035, 601.173, 606.311, 611.45, 616.588, 621.726, 626.864, 632.003, 637.141, 642.279, 647.417, 652.555, 657.694, 662.832, 667.97, 673.108, 678.247, 683.385, 688.523, 693.661, 698.8, 703.938, 709.076, 714.214, 719.352, 724.491, 729.629, 734.767, 739.905, 745.044, 750.182, 755.32, 760.458, 765.597, 770.735, 775.873, 781.011, 786.149, 791.288, 796.426, 801.564, 806.702, 811.841, 816.979, 822.117, 827.255, 832.394, 837.532, 842.67, 847.808, 852.947, 858.085, 863.223, 868.361, 873.499, 878.638, 883.776, 888.914, 894.052, 899.191, 904.329, 909.467, 914.605, 919.744, 924.882, 930.02, 935.158, 940.296, 945.435, 950.573, 955.711, 960.849, 965.988, 971.126, 976.264, 981.402, 986.541, 991.679, 996.817, 1001.955, 1007.093, 1012.232, 1017.37, 1022.508, 1027.646, 1032.785, 1037.923, 1043.061, 1048.199, 1053.338, 1058.476, 1063.614, 1068.752, 1073.89, 1079.029, 1084.167, 1089.305, 1094.443, 1099.582, 1104.72, 1109.858, 1114.996, 1120.135, 1125.273, 1130.411, 1135.549, 1140.688, 1145.826, 1150.964, 1156.102, 1161.24, 1166.379, 1171.517, 1176.655, 1181.793, 1186.932, 1192.07, 1197.208, 1202.346, 1207.485, 1212.623, 1217.761, 1222.899, 1228.037, 1233.176, 1238.314, 1243.452, 1248.59, 1253.729, 1258.867, 1264.005, 1269.143, 1274.282, 1279.42, 1284.558, 1289.696, 1294.834, 1299.973, 1305.111, 1310.249, 1315.387, 1320.526, 1325.664, 1330.802, 1335.94, 1341.079, 1346.217, 1351.355, 1356.493, 1361.631, 1366.77, 1371.908, 1377.046, 1382.184, 1387.323, 1392.461, 1397.599, 1402.737, 1407.876, 1413.014, 1418.152, 1423.29, 1428.428, 1433.567, 1438.705, 1443.843, 1448.981, 1454.12, 1459.258, 1464.396, 1469.534, 1474.673, 1479.811, 1484.949, 1490.087, 1495.226, 1500.364, 1505.502, 1510.64, 1515.778, 1520.917, 1526.055, 1531.193, 1536.331, 1541.47, 1546.608, 1551.746, 1556.884, 1562.023, 1567.161, 1572.299, 1577.437, 1582.575, 1587.714, 1592.852, 1597.99, 1603.128, 1608.267, 1613.405, 1618.543, 1623.681, 1628.82, 1633.958, 1639.096, 1644.234, 1649.372, 1654.511, 1659.649, 1664.787, 1669.925, 1675.064, 1680.202, 1685.34, 1690.478, 1695.617, 1700.755, 1705.893, 1711.031, 1716.169, 1721.308, 1726.446, 1731.584, 1736.722, 1741.861, 1746.999, 1752.137, 1757.275, 1762.414, 1767.552, 1772.69, 1777.828, 1782.967, 1788.105, 1793.243, 1798.381, 1803.519, 1808.658, 1813.796, 1818.934, 1824.072, 1829.211, 1834.349, 1839.487, 1844.625, 1849.764, 1854.902, 1860.04, 1865.178, 1870.316, 1875.455, 1880.593, 1885.731, 1890.869, 1896.008, 1901.146, 1906.284, 1911.422, 1916.561, 1921.699, 1926.837, 1931.975, 1937.113, 1942.252, 1947.39, 1952.528, 1957.666, 1962.805, 1967.943, 1973.081, 1978.219, 1983.358, 1988.496, 1993.634, 1998.772, 2003.91, 2009.049, 2014.187, 2019.325, 2024.463, 2029.602, 2034.74, 2039.878, 2045.016, 2050.155, 2055.293, 2060.431, 2065.569, 2070.707, 2075.846, 2080.984, 2086.122, 2091.26, 2096.399, 2101.537, 2106.675, 2111.813, 2116.952, 2122.09, 2127.228, 2132.366, 2137.505, 2142.643, 2147.781, 2152.919, 2158.057, 2163.196, 2168.334, 2173.472, 2178.61, 2183.749, 2188.887, 2194.025, 2199.163, 2204.302, 2209.44, 2214.578, 2219.716, 2224.854, 2229.993, 2235.131, 2240.269, 2245.407, 2250.546, 2255.684, 2260.822, 2265.96, 2271.099, 2276.237, 2281.375, 2286.513, 2291.651, 2296.79, 2301.928, 2307.066, 2312.204, 2317.343, 2322.481, 2327.619, 2332.757, 2337.896, 2343.034, 2348.172, 2353.31, 2358.448, 2363.587, 2368.725, 2373.863, 2379.001, 2384.14, 2389.278, 2394.416, 2399.554, 2404.693, 2409.831, 2414.969, 2420.107, 2425.246, 2430.384, 2435.522, 2440.66, 2445.798, 2450.937, 2456.075, 2461.213, 2466.351, 2471.49, 2476.628, 2481.766, 2486.904, 2492.043, 2497.181, 2502.319, 2507.457, 2512.595, 2517.734, 2522.872, 2528.01, 2533.148, 2538.287, 2543.425, 2548.563, 2553.701, 2558.84, 2563.978, 2569.116, 2574.254, 2579.392, 2584.531, 2589.669, 2594.807, 2599.945, 2605.084, 2610.222, 2615.36, 2620.498, 2625.637, 2630.775, 2635.913, 2641.051, 2646.189, 2651.328, 2656.466, 2661.604, 2666.742, 2671.881, 2677.019, 2682.157, 2687.295, 2692.434, 2697.572, 2702.71, 2707.848, 2712.986, 2718.125, 2723.263, 2728.401, 2733.539, 2738.678, 2743.816, 2748.954, 2754.092, 2759.231, 2764.369, 2769.507, 2774.645, 2779.784, 2784.922, 2790.06, 2795.198, 2800.336, 2805.475, 2810.613, 2815.751, 2820.889, 2826.028, 2831.166, 2836.304, 2841.442, 2846.581, 2851.719, 2856.857, 2861.995, 2867.133, 2872.272, 2877.41, 2882.548, 2887.686, 2892.825, 2897.963, 2903.101, 2908.239, 2913.378, 2918.516, 2923.654, 2928.792, 2933.93, 2939.069, 2944.207, 2949.345, 2954.483, 2959.622, 2964.76, 2969.898, 2975.036, 2980.175, 2985.313, 2990.451, 2995.589, 3000.727, 3005.866, 3011.004, 3016.142, 3021.28, 3026.419, 3031.557, 3036.695, 3041.833, 3046.972, 3052.11, 3057.248, 3062.386, 3067.525, 3072.663, 3077.801, 3082.939, 3088.077, 3093.216, 3098.354, 3103.492, 3108.63, 3113.769, 3118.907, 3124.045, 3129.183, 3134.322, 3139.46, 3144.598, 3149.736, 3154.874, 3160.013, 3165.151, 3170.289, 3175.427, 3180.566, 3185.704, 3190.842, 3195.98, 3201.119, 3206.257, 3211.395, 3216.533, 3221.671, 3226.81, 3231.948, 3237.086, 3242.224, 3247.363, 3252.501, 3257.639, 3262.777, 3267.916, 3273.054, 3278.192, 3283.33, 3288.468, 3293.607, 3298.745, 3303.883, 3309.021, 3314.16, 3319.298, 3324.436, 3329.574, 3334.713, 3339.851, 3344.989, 3350.127, 3355.265, 3360.404, 3365.542, 3370.68, 3375.818, 3380.957, 3386.095, 3391.233, 3396.371, 3401.51, 3406.648, 3411.786, 3416.924, 3422.063, 3427.201, 3432.339, 3437.477, 3442.615, 3447.754, 3452.892, 3458.03, 3463.168, 3468.307, 3473.445, 3478.583, 3483.721, 3488.86, 3493.998, 3499.136, 3504.274, 3509.412, 3514.551, 3519.689, 3524.827, 3529.965, 3535.104, 3540.242, 3545.38, 3550.518, 3555.657, 3560.795, 3565.933, 3571.071, 3576.209, 3581.348, 3586.486, 3591.624, 3596.762, 3601.901, 3607.039, 3612.177, 3617.315, 3622.454, 3627.592, 3632.73, 3637.868, 3643.006, 3648.145, 3653.283, 3658.421, 3663.559, 3668.698, 3673.836, 3678.974, 3684.112, 3689.251, 3694.389, 3699.527, 3704.665, 3709.804, 3714.942, 3720.08, 3725.218, 3730.356, 3735.495, 3740.633, 3745.771, 3750.909, 3756.048, 3761.186, 3766.324, 3771.462, 3776.601, 3781.739, 3786.877, 3792.015, 3797.153, 3802.292, 3807.43, 3812.568, 3817.706, 3822.845, 3827.983, 3833.121, 3838.259, 3843.398, 3848.536, 3853.674, 3858.812, 3863.95, 3869.089, 3874.227, 3879.365, 3884.503, 3889.642, 3894.78, 3899.918, 3905.056, 3910.195, 3915.333, 3920.471, 3925.609, 3930.747]

# histogram fractions for inter-transaction time, in seconds
time_dist = [0.5625408172580634, 0.3513233569517496, 0.05484435018925163, 0.014592389205283596, 0.00634466970499217, 0.0, 0.0033742266665730356, 0.0021734092680631726, 0.0013342415538998475, 0.0010463262712161962, 0.0, 0.0007022323967893935, 0.0004845403537846815, 0.0003019599306194392, 0.000214180881020765, 0.0, 0.00019662507110103017, 0.00011586834547024992, 8.075672563078025e-05, 9.129021158262115e-05, 0.0, 4.915626777525754e-05, 3.1600457855522703e-05, 4.213394380736361e-05, 2.457813388762877e-05, 0.0, 1.7555809919734836e-05, 1.404464793578787e-05, 3.5111619839469674e-06, 7.022323967893935e-06, 0.0, 7.022323967893935e-06, 1.404464793578787e-05, 3.5111619839469674e-06, 1.0533485951840902e-05, 0.0, 0.0, 0.0, 0.0]

# histogram bins for inter-transaction time, in seconds
time_bins = [0.8, 1.6, 2.4, 3.2, 4.0, 4.8, 5.6, 6.4, 7.2, 8.0, 8.8, 9.6, 10.4, 11.2, 12.0, 12.8, 13.6, 14.4, 15.2, 16.0, 16.8, 17.6, 18.4, 19.2, 20.0, 20.8, 21.6, 22.4, 23.2, 24.0, 24.8, 25.6, 26.4, 27.2, 28.0, 28.8, 29.6, 30.4, 31.2]