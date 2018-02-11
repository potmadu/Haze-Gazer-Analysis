metadata = read.csv("C:/Datasets/Haze_Gazer/Instagram-Haze/All-Data-Tagged.csv",stringsAsFactors=FALSE);
results = read.csv("C:/Users/Fox/Documents/GitHub/Haze-Gazer-Analysis/AOD-Net/test/output_aod_all.csv",stringsAsFactors=FALSE);

metadata$id = paste(metadata$id,".jpg",sep="");

metadata$waktu = as.POSIXlt(as.numeric(metadata$timestamp),origin="1970-01-01");

library(dplyr);

metadata_results = metadata %>%
select(-waktu) %>%
left_join(results,c("id"="id_image")) %>%
as.data.frame();

metadata_results$waktu = metadata$waktu;

write.csv(metadata_results,"C:/Users/Fox/Documents/GitHub/Haze-Gazer-Analysis/AOD-Net/test/join_results.csv");

