emails = "pamousset@kliper.io,mfoureaux@kliper.io,eaguilar@kliper.io,lgabriel@kliper.io,nbazin@kliper.io,iberrada@kliper.io,bjoubel@kliper.io,groux@kliper.io,arambaud@kliper.io,jlijeour@kliper.io,rphilbert@kliper.io,cpratt@kliper.io,lleblan@kliper.io,zrouchi@kliper.io,msaute@kliper.io"
email_list = emails.split(",")
print(email_list)
or_format = " OR ".join(email_list)
print(or_format)