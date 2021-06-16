這個作業是當OpenMV掃到April tag之後，車子就會走到april tag前面，而且與april tag垂直。之後再利用PING來計算OpenMV和April tag的距離。

main.cpp裏是包括UART和RPC的設定，還有用PING獲取距離的程式。

main.py就是操作車子移動的rpc指令。
以下當OpenMV掃到april tag之後車子所進行的步驟：
1.轉彎至與april tag平行
2.直走到april tag面前
3.轉90度來面向april tag


如果車子與april tag之間的差角為theta，與april tag的距離為a
1.我利用turn的factor來改變車子所需轉的調度為90-theta。
2.所需前進的距離為a*sin(theta)，利用所計算后的距離再配合環境的參數（輪子摩檫力/轉速/轉彎前進的距離....)做scaling
3.然後利用turn來讓車子轉90度

如果與april tag之間的距離太小，那就不需要前進，只需要轉彎就能面向april tag。

面向april tag之後，車子的PING就能計算OpenMV和april tag之間的距離。

附件是車子前進的簡圖
