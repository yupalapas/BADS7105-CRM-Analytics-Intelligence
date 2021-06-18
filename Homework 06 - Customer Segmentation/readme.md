Customer Segmentation
------------------------------------
นำข้อมูล transaction ของ Supermarket มาลองจัดกลุ่มดู โดยเริ่มแรกจะ Import เข้า Google Big Query แล้วนำข้อมูลสร้าง Model K-Mean Clustering แล้วลองวิเคราะห์ 

**Procedure**
  1. Create a cluster for each of the threr groups
  2. The clustering method is defined as Random
  3. Define the Euclidean distance type. As shown in the image below
  
![image](https://user-images.githubusercontent.com/77535395/122580384-1a443100-d080-11eb-9671-dc5d3a70595e.png)

  4. SQL codind to create KMean model for customer segmentation
![image](https://user-images.githubusercontent.com/77535395/122580594-4fe91a00-d080-11eb-9adc-9e7c40d49e7f.png)

  5. the customer segmentation result is shown below
![image](https://user-images.githubusercontent.com/77535395/122580816-92aaf200-d080-11eb-9de2-22ad29e28858.png)
![image](https://user-images.githubusercontent.com/77535395/122580927-b2421a80-d080-11eb-82fd-18fc89c8bfc9.png)
![image](https://user-images.githubusercontent.com/77535395/122580977-bec67300-d080-11eb-885a-7dc37f7eda53.png)
