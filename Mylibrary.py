class SubfieldsInAI:
    def Subfields():
        l_list =["Sub-fields in AI are:","Machine Learning ","Neural Networks ","Vision ","Robotics ","Speech Processing ","Natural Language Processing"];
        for i in l_list:
            print(i);
    def OddEven():
        a=int(input("Enter a number:"))
        if (a%2==0):
            print(a," is Even number ");
        else:
            print(a," is odd number ");        
    def Elegible():
        a=input("Your Gender:");
        b=int(input("Your Age:"));
        if (b>27):
            print("You are ELIGIBLE!");
        else:
            print("NOT ELIGIBLE!");
    def Elegibleboth():
        a=input("Your Gender:")
        b=int(input("Your Age:"))
        if (a=='Male'and b>=27):
            print("You are ELIGIBLE!")
        elif(a=='FeMale'and b>=24):
            print("You are ELIGIBLE!")
        elif(a=='Male'and b<27):
            print("Not ELIGIBLE!")
        elif(a=='FeMale'and b<24):
            print("Not ELIGIBLE!");
    def percentage(i,j,k,l,m): 
         print("Subject1=",i);
         print("Subject2=",j);
         print("Subject3=",k);
         print("Subject4=",l);
         print("Subject5=",m);
         total=i+j+k+l+m;
         average=total/5;
         print("Total :",total);
         print("Percentage : ",average);
    def triangle1():
        a=int(input("Height:"))
        b=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2");
        print("Area of Triangle:",(a*b)/2);
        c=int(input("Height1:"))
        d=int(input("Height2:"))
        e=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth");
        print("Perimeter of Triangle:",(c+d+e));    