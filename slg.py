
import csv
import sys
#replace the name with your actual csv file name
file_name = "master.csv" 
f1 = open(file_name)
csv_file = csv.reader(f1)

org = [] #empty list to store second column values
link= []
lid= []
for line in csv_file:
    org.append(line[0])
    link.append(line[8])
    lid.append(line[10])
    file_name1 = "CSV/"+line[0]+"/SGD.csv" 
    f2 = open(file_name1)
    csv_file1 = csv.reader(f2)
    jsl=[]
    table_code=""
    if (line[10]=="bigg"):
        for line1 in csv_file1:
            jsl.append(line1[0])
            table_code=table_code+"<tr><td><a href='"+line[8]+"/genes/"+line1[0]+"' target='blank'><center><u><font color='black'>"+line1[0]+"</font></u></center></a></td></tr>"
    elif (line[10]=="vmh"):
        for line1 in csv_file1:
            jsl.append(line1[0])
            table_code=table_code+"<tr><td><a href='https://vmh.life/#microbegene/"+line1[0]+"' target='blank'><center><u><font color='black'>"+line1[0]+"</font></u></center></a></td></tr>"
    #print("jsl")
    #print(jsl)
#a = "../assets/img/s.jpg"

    #print(line[0])
    filename='Single_Lethal_Gene/'+line[0]+'.html' 
    #print(filename)
    f = open(filename,'w')
    message ="""<!doctype html>
<html lang="en">
<head>
  
    <title>CASTLE</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link href="https://fonts.googleapis.com/css?family=Muli:400,700|Hepta+Slab:400,700&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="../fonts/icomoon/style.css">

    <link rel="stylesheet" href="../css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/bootstrap-datepicker.css">
    <link rel="stylesheet" href="../css/jquery.fancybox.min.css">
    <link rel="stylesheet" href="../css/owl.carousel.min.css">
    <link rel="stylesheet" href="../css/owl.theme.default.min.css">
    <link rel="stylesheet" href="../fonts/flaticon/font/flaticon.css">
    <link rel="stylesheet" href="../css/aos.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-csv/0.71/jquery.csv-0.71.min.js"></script>
    <!-- MAIN CSS -->
    <link rel="stylesheet" href="../css/style.css">
    <style>
   table.minimalistBlack {{
  border: 2.5px solid #000000;
  width: 60%;
  text-align: left;
  border-collapse: collapse;
}}
table.minimalistBlack td, table.minimalistBlack th {{
  border: 1.5px solid #000000;
  padding: 5px 5px;
}}
table.minimalistBlack  td {{
  font-size: 16px;
  width:200px;
}}
.footer {{
  background-color: #777;
  padding: 10px;
  text-align: center;
  color: white;
}}

</style>
  </head>

  <body data-spy="scroll" data-target=".site-navbar-target" data-offset="300" background="../images/body2.jpg">

    
    <div class="site-wrap" id="home-section">

      <div class="site-mobile-menu site-navbar-target">
        <div class="site-mobile-menu-header">
          <div class="site-mobile-menu-close mt-3">
            <span class="icon-close2 js-menu-toggle"></span>
          </div>
        </div>
        <div class="site-mobile-menu-body"></div>
      </div>



      <header class="site-navbar site-navbar-target" role="banner">

        <div class="container">
          <div class="row align-items-center position-relative">

            <div class="col-3 ">
              <div class="site-logo">
                <a href="../index.html" class="font-weight-bold"><img src=""></a>
              </div>
            </div>

            <div class="col-9  text-right">
              

              <span class="d-inline-block d-lg-none"><a href="#" class="text-white site-menu-toggle js-menu-toggle py-5 text-white"><span class="icon-menu h3 text-white"></span></a></span>

              

              <nav class="site-navigation text-right ml-auto d-none d-lg-block" role="navigation">
                <ul class="site-menu main-menu js-clone-nav ml-auto ">
                  <li class="active"><a href="../index.html" class="nav-link">Home</a></li>
                  <li><a href="../about.html" class="nav-link">About</a></li>
                  <li><a href="../contact.html" class="nav-link">Contact</a></li>
                </ul>
              </nav>
            </div>

            
          </div>
        </div>

      </header>
      <div class="site-section">
            <div class="container">
      
              <div>
                <div>
               <center> 
               <font size="8" color="marooon"><b><center><i>{}</i></center></b></font>
                <font size="4" color="darkblue"><b><center>SINGLE LETHAL GENES</center></b></font><br>
                <table border=1 align="center">{}</table>
                </center>
                </div>
            </div>
                
          </DIV>
            <br>
            <br>
  
          <div class="footer">
             <p><p align="center"> Copyright &copy; CASTLE <script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="icon-heart text-danger" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank" >Colorlib</a></p></p>
           </div>
          </div> <!-- END .site-section -->"""
    newmsg = message.format(line[11],table_code)
  
#print(message)
    f.write(newmsg)
    f.close()
f1.close()
