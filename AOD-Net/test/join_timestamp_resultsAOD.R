metadata_file="E:/Datasets/Haze-Gazer-Analysis/Instagram-Haze/All Data.csv";
result_file="E:/GitHub/Haze-Gazer-Analysis/Results/output_aod_all.csv";

output_file="E:/GitHub/Haze-Gazer-Analysis/Results/join_aod_all.csv";

metadata = read.csv(metadata_file,stringsAsFactors=FALSE);
results = read.csv(result_file,stringsAsFactors=FALSE);

metadata$id = paste(metadata$id,".jpg",sep="");

#metadata$waktu = as.POSIXlt(as.numeric(metadata$timestamp),origin="1970-01-01");

library(dplyr);

metadata_results = results %>%
left_join(metadata,c("X0"="id")) %>%
as.data.frame();

metadata_results$waktu = as.POSIXlt(as.numeric(metadata_results$timestamp),origin="1970-01-01");

write.csv(metadata_results,output_file);

isOutdoor_file = "E:/GitHub/Haze-Gazer-Analysis/Results/output_places365_classification.csv";

isOutdoor = read.csv(isOutdoor_file,stringsAsFactors=FALSE);

metadata_result_isOutdoor = metadata_results %>%
select(-waktu) %>%
left_join(isOutdoor,c("X0"="X0")) %>%
as.data.frame();

metadata_result_isOutdoor$waktu = as.POSIXlt(as.numeric(metadata_result_isOutdoor$timestamp),origin="1970-01-01");

write.csv(metadata_result_isOutdoor,output_file);

