import pandas as pd
my_blog_visitor =  pd.DataFrame({ "day":[1,2,3,4,5],"visitors" :[100,12322,1000]
},index=[2000,2002,2003,2004])

next_blog_visitor = pd.DataFrame({
                     "day":[1,2,3,4,5],
                      "visitors" :[100,12322,1000]},index=[2005,2006,2007,2008])
#df = pd.DataFrame(my_blog_visitor)
#print(df)

#print(df.head(2))
#print(df.tail(2))
#print()

merged = pd.merge(my_blog_visitor,next_blog_visitor)
join = my_blog_visitor.join(next_blog_visitor)
print (merged)