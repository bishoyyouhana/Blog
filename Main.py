import os
import datetime

OGcontent='''
<head>
    <meta charset="utf-8">
    <title>My Blog!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {{
            padding-top: 80px;
        }}
        .t {{
        padding-top: 60px; 
        font-size: 50px; 
        }}
    </style>
</head>
<!DOCTYPE html>
<html>
  <body>
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
            <a class="navbar-brand" href="#">Bishoy Youhana Portfolio</a>
      </div>
      <div>
      <h class="t"><center>Blog</center></h>
      </div>
    </div>
    <div class="container">
        {blog}
    </div>
  </body>
</html>
'''
update_body='''
<div style="padding-top:50px">
    <p style="font-size: 10px">{post_date}</p>
    <p id="paddingtop" style="font-size: 22px">
        {blog_update}
    </p>
</div>
'''
'''
def line_pre_adder(filename, line_to_prepend):
    f = fileinput.input(filename, inplace=1)
    for xline in f:
        if f.isfirstline():
            print line_to_prepend.rstrip('\r\n') + '\n' + xline,
        else:
            print xline
'''
now = datetime.datetime.today()
now = str(now)
content = " "
def get_text():
    return input("Enter Blog Update:")
os.chdir(r"C:\Users\Win8.1\source\repos\Portfolio\Blog")

with open('Blog.txt', 'r') as fp:
    read_lines = fp.readlines()
    read_lines = [line.rstrip('\n') for line in read_lines]

listPosts =[]
for g in read_lines:
    postData = g.split("--")
    postText = postData[0]
    postDate = postData[1]
    dataTup= (postText,postDate)
    listPosts.append(dataTup)
    content += update_body.format(blog_update=postText, post_date=postDate)
Update = get_text()
dataTup = (Update, now)
listPosts.append(dataTup)
content += update_body.format(blog_update=Update, post_date=now)

blog_file= open("Blog.txt","a")

whole_thing="{} -- {}"
blog_file.write("\n")
blog_file.write(whole_thing.format(Update,now))
blog_file.close()
OGcontent = OGcontent.format(blog=content)

os.chdir(r"C:\Users\Win8.1\source\repos\Portfolio\Blog")
indexFile = open("index.html","w")
indexFile.write(OGcontent)

indexFile.close()
input("press enter")