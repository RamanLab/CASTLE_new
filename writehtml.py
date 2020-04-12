
import csv
import sys
#replace the name with your actual csv file name
file_name = "master.csv" 
f1 = open(file_name)
csv_file = csv.reader(f1)

organism = [] #empty list to store second column values
jsl=[]
jdl=[]
jtl=[]
sgd=[]
dgd=[]
tgd=[]
gr=[]
link=[]
hp=[]
org=[]
for line in csv_file:
    organism.append(line[0])
    jsl.append(line[1])
    jdl.append(line[2])
    jtl.append(line[3])
    sgd.append(line[4])
    dgd.append(line[5])
    tgd.append(line[6])
    gr.append(line[7])
    link.append(line[8])
    hp.append(line[9])
    org.append(line[11])

#a = "../assets/img/s.jpg"

    print(line[0])
    filename='Synthetic_lethal/'+line[0]+'.html'
    print(filename)
    f = open(filename,'w')
    message ="""
    <!doctype html>
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

  <body data-spy="scroll" data-target=".site-navbar-target" data-offset="300" >

    
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
                <a href="index.html" class="font-weight-bold"><img src=""></a>
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
                <br>
                <font size="10" color="marooon"><b><center><i>{org:}</i></center></b></font>
                </div>
            </div>
                <font size=5><br>Growth Rate: {gr:}
                    <br>
                    Human Pathogen: {hp:}
                  </font>
                    <br>
                   <br>
                    <table class="minimalistBlack" border="0" align="center">
                        <tr><td><center><a href="../Single_Lethal_Reaction/{organism:}.html"><font color="maroon"><u>Single lethal reactions</u>
                            <br> (Jsl)</font></a></center></td>
                        <td> <p><a href="../CSV/{organism:}/JSL.csv" download="{organism:}_Jsl.csv"><center><abbr title='Download the Jsl CSV file'><img src='../images/csv.jpg' height='35' width='35'></abbr></a></p></td>
                          <td> <p><a href="../json/{organism:}/JSL.json" download="{organism:}_Jsl.json"><center><abbr title='Download the Jsl JSON file'><img src='../images/json.png' height='35' width='27 '></abbr></a></p></td>
                            <td rowspan="3"><p><a href="../mat/{organism:}/{organism:}.matRxn_lethals.mat" download="{organism:}.matRxn_lethals.mat"><center><abbr title='Download all the Lethal Reactions MAT file'><img src='../images/matlab.png' height='65' width='70 '></abbr></a>
                              <br><font size="2">(Combined download <br>
                                of Jsl, Jdl and Jtl)</font></p></td>
                        
                        </tr>
                            <tr><td><center><a href="../Double_Lethal_Reaction/{organism:}.html"><font color="maroon"><u>Double lethal reactions</u>
                            <br> (Jdl)</font></a></center> </td>
                              <td> <p><a href="../CSV/{organism:}/JDL.csv" download="{organism:}_Jdl.csv"><center><abbr title='Download the Jdl CSV file'><img src='../images/csv.jpg' height='35' width='35'></abbr></a></p></td>
                                <td> <p><a href="../json/{organism:}/JDL.json" download="{organism:}_Jdl.json"><center><abbr title='Download the Jdl JSON file'><img src='../images/json.png' height='35' width='27 '></abbr></a></p></td>
                               


                        </tr>
                        <tr><td><center><a href="../Triple_Lethal_Reaction/{organism:}.html"><font color="maroon"><u>Triple lethal<br>reactions</u>
                            <br> (Jtl)</font></a></center> </td>
                          <td> <p><a href="../CSV/{organism:}/JTL.csv" download="{organism:}_Jtl.csv"><center><abbr title='Download the Jtl CSV file'><img src='../images/csv.jpg' height='35' width='35'></abbr></a></p></td>
                            <td> <p><a href="../json/{organism:}/JTL.json" download="{organism:}_Jtl.json"><center><abbr title='Download the Jtl JSON file'><img src='../images/json.png' height='35' width='27 '></abbr></a></p></td>
                           
                        </tr>
                        <tr><td><center><a href="../Single_Lethal_Gene/{organism:}.html"><font color="maroon"><u>Single lethal genes</u>
                            <br> (Sgd)</font></a></center> </td>
                          <td> <p><a href="../CSV/{organism:}/SGD.csv" download="{organism:}_Sgd.csv"><center><abbr title='Download the Sgd CSV file'><img src='../images/csv.jpg' height='35' width='35'></abbr></a></p></td>
                            <td> <p><a href="../json/{organism:}/SGD.json" download="{organism:}_Sgd.json"><center><abbr title='Download the Sgd JSON file'><img src='../images/json.png' height='35' width='27 '></abbr></a></p></td>
                              <td rowspan="3"><p><a href="../mat/{organism:}/{organism:}.mat_gene_lethals.mat" download="{organism:}.mat_gene_lethals.mat"><center><abbr title='Download all the Lethal Genes MAT file'><img src='../images/matlab.png' height='65' width='70 '></abbr></a>
                                <br><font size="2">(Combined download <br>of Sgd, Dgd and Tgd)</font></p></td>
                        </tr>
                        <tr><td><center><a href="../Double_Lethal_Gene/{organism:}.html"><font color="maroon"><u>Double lethal genes</u>
                            <br> (Dgd)</font></a></center> </td>
                          <td> <p><a href="../CSV/{organism:}/DGD.csv" download="{organism:}_Dgd.csv"><center><abbr title='Download the Dgd CSV file'><img src='../images/csv.jpg' height='35' width='35'></abbr></a></p></td>
                            <td> <p><a href="../json/{organism:}/DGD.json" download="{organism:}_Dgd.json"><center><abbr title='Download the Dgd JSON file'><img src='../images/json.png' height='35' width='27 '></abbr></a></p></td>
                           
                        </tr>
                        <tr><td><center><a href="../Triple_Lethal_Gene/{organism:}.html"><font color="maroon"><u>Triple lethal genes</u><br>(Tgd)</font></a>
                            </center> </td>
                          <td> <p><a href="../CSV/{organism:}/TGD.csv" download="{organism:}_Tgd.csv"><center><abbr title='Download the Tgd CSV file'><img src='../images/csv.jpg' height='35' width='35'></abbr></a></p></td>
                            <td> <p><a href="../json/{organism:}/TGD.json" download="{organism:}_Tgd.json"><center><abbr title='Download the Tgd JSON file'><img src='../images/json.png' height='35' width='27 '></abbr></a></p></td>
                           
                        </tr>
                    
                    </table>
               
               <br>
                    <font size=5>Model Link:<a href="{link:}"> <font color="black"><u>{link:}</u></font></a>
                      </font>
                        <br>
             <br><br>
             
            </div>
            
  
          <div class="footer">
             <p><p align="center"> Copyright &copy; CASTLE <script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="icon-heart text-danger" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank" >Colorlib</a></p></p>
           </div>
          </div> <!-- END .site-section -->

    
    """    
    newmsg = message.format(org=line[11],organism = line[0],gr = line[7],hp = line[9],link = line[8])
    f.write(newmsg)
    f.close()
f1.close()
