**Product Recommendation using items-based collaborative filtering**
--------------------------------------------
Collaborative filtering is a correlation rule-based algorithm. The following example shows how collaborative filtering predicts the interests of customers A and B in products a, b, and c. If both customers A and B have purchased products X and Y, collaborative filtering determines that customers A and B have similar interests in shopping. Collaborative filtering then recommends product Z to customer B because customer A has purchased product Z. This is a classic example of using features of users as a correlation.

**Step**
1. Import dataset 'Customer Survey'
2. Check missing, remove null data and drop column for item-item collaborating
3. Convert string to value
4. list all product, sorting and visualisation for Top15
![image](https://user-images.githubusercontent.com/77535395/122405412-3d9cac80-cfaa-11eb-8644-175863408355.png)

5. Create blank item-item matrix
![image](https://user-images.githubusercontent.com/77535395/122405072-f1ea0300-cfa9-11eb-8c7b-7ae8e1f5bc48.png)

6. Calculate cosine similarity and filter to address weak link
![image](https://user-images.githubusercontent.com/77535395/122405196-0b8b4a80-cfaa-11eb-9528-820fdd4151c8.png)
![image](https://user-images.githubusercontent.com/77535395/122405348-2bbb0980-cfaa-11eb-8087-84dd1809c40d.png)

7. Bulid network graph
![image](https://user-images.githubusercontent.com/77535395/122405548-57d68a80-cfaa-11eb-89d4-6528e15a0ba4.png)

8. Interpret result
![image](https://user-images.githubusercontent.com/77535395/122405641-69b82d80-cfaa-11eb-942f-e696153613a3.png)


