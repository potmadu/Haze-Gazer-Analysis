metadata_file="E:/Datasets/Haze-Gazer-Analysis/Instagram-Haze/All Data.csv";
result_file="E:/GitHub/Haze-Gazer-Analysis/AOD-Net/test/output_aod_non-haze-no-landscapes.csv";
output_file="E:/GitHub/Haze-Gazer-Analysis/AOD-Net/test/join_aod_non-haze-no-landscapes.csv";

metadata = read.csv(metadata_file,stringsAsFactors=FALSE);
results = read.csv(result_file,stringsAsFactors=FALSE);

metadata$id = paste(metadata$id,".jpg",sep="");

metadata$waktu = as.POSIXlt(as.numeric(metadata$timestamp),origin="1970-01-01");

library(dplyr);

metadata_results = results %>%
left_join(metadata %>% select(-waktu),c("id_image"="id")) %>%
as.data.frame();

metadata_results$waktu = as.POSIXlt(as.numeric(metadata_results$timestamp),origin="1970-01-01");

write.csv(metadata_results,output_file);

