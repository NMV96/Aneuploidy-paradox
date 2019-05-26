options(echo=TRUE)
setwd("/home/nelli/data/cancer_files/nsclc/")
filenames <- dir(path="alignments1", pattern = "*.sam", recursive = FALSE )
bam<-paste0("alignments1/",sub(".sam",".bam",filenames))
pos<- read.table("/data/nelli/cancer_files/my.gtf",header=FALSE,colClasses = "character")
dir.create('aligns1')
dir.create('statistics1')
for(i in 1:nrow(pos)){
  for(b in bam){
    if(!file.exists(paste0(b,".bai"))) system(paste("samtools view -uh -f 03 ",sub(".bam",".sam",b)," | samtools sort - -O bam -o ",b," ; samtools index",b),intern=TRUE)
    system(paste0("samtools idxstats ",b," > statistics1/",sub("alignments1","",sub(".bam","_statistics.txt",b))),intern=TRUE)
    html<-paste0("aligns1/chr",pos[i,1],"_",pos[i,4],"-",pos[i,5],"_",pos[i,16],"_",sub(".bam","",basename(b)),".html")
    system(paste0("samtools tview -p ",pos[i,1],":",pos[i,4],"-",pos[i,5]," -d H ",b," /data/db/homo_sapiens/homo_sapiens.fa > ",html))
    if(length(grep("'tviewc",readLines(html,warn=FALSE),fixed = TRUE))==0) file.remove(html)
  }
}
