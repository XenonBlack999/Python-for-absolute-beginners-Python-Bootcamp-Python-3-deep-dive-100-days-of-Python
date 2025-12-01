꧁༒༺ Bitwise OPerator ༻༒꧂

• AND (&)
• OR (|)
• XOR (^)
• NOT (~)
• Left Shift (<<)
• Right Shift (>>)

╚»★«╝ Decimal To Binary Changing in Math ╚»★«╝
Decimal ကို ၂နဲ့စားအကြွမ်းတိုင်းကို နောက်ဆုံးအကြွမ်းက စစီရင်binary
1 byte =  8 bit
1 bit = 1 binary number

2 | 10       = 0
2 | 5          = 1
2 | 2           = 0
1

So ,    10 (Decimal )  = 1010 (binary number )
( 8 bit  )00001010




✎﹏﹏Bitwise AND (&):﹏﹏

Usage :

True & True = True 
1 	& 1 = 1
False & True  = False 
1 & 0 = 0 

#Bit by bit operation 
Decimal ကို binary ပြောင်းပြီးမှOperationလုပ်တယ်



▄︻┻ Bitwise OR (|): ︻┳═─-
Usage :
True or True  = True 
1 | 1 = 1
False  or False = False 
0 | 0 = 0
True or False = True 
1 | 0 = 1



★彡 Bitwise XOR (^): 彡★
Usage :
True XOR TRUE = 
1  ^ 1 = 0
False XOR TRUE =
0 ^  1 =1
False XOR False =
0 ^ 0 = 0




▄︻┻ Bitwise NOT (~): ︻┳═─-
NOT အော်ပရေတာသည် ဂဏန်းတစ်ခု၏ bits အားလုံးကို လှန်သည်။ ၎င်းသည် 1 မှ 0 နှင့် 0 မှ 1 သို့ပြောင်းသည်။ ၎င်းကို one's complement ဟုခေါ်သည်။


╰☆☆ Bitwise Left Shift (<<): ☆☆╮
Usage : 

x = 10 (binary 00001010)
y = x << 2

if we do right shift we will remove  two number  from the end of left  side 
so we will get

x = 20 ( binary 10100)



╰☆☆ Bitwise Right  Shift (>>): ☆☆╮
Usage :

x = 10 (binary 00001010)
y = x >> 2

if we do right shift we will remove  10 from the end of right side 
so we will get

y = 2 (00000010)