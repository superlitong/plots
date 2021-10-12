library(reshape2)
library(ggplot2)
library(scales)
windowsFonts(myFont = windowsFont("Times new roman"))  
#size_throughput1.csv size_throughput2.csv size_throughput3.csv
df <- read.csv("loss3.csv")

df2 <- df
levels(df2$size)[levels(df2$size)=="1000Mbps"] <- "1Gbps"
levels(df2$type)[levels(df2$type)=="FillP-ssd"] <- "FillP-d"

bp <- ggplot(df2, aes(x=size, y=Throughput, group=size)) + geom_boxplot(aes(fill=size))
bp <- bp + coord_flip()
#bp <- bp+ scale_x_discrete(limits=c("CUBIC", "BBR", "FillP"))

bp <- bp + facet_grid(type ~ .,scales="free_y")
bp <- bp + labs(title="",x="", y = "Packet Loss Ratio with Log Scale (%)")
bp <- bp + scale_y_continuous(trans='log',
	labels=c("0.01", "0.05", "0.5", "1", "3","10"),
	breaks=c(0.01, 0.05, 0.5,1, 3, 10))


bp <- bp + theme(strip.text.y = element_text(family = "myFont", size=16, face="bold"),
      strip.background = element_rect(fill="#BBBBBB"))
bp <- bp + theme(axis.text= element_text(family = "myFont",colour="#666666", size=16, face="bold"))   
bp <- bp + theme(axis.title= element_text(family = "myFont", size=16, face="bold"))    

bp <- bp + theme(axis.title.y= element_blank(),panel.grid=element_line(size=2), panel.spacing=unit(0.4, "lines"))
bp <- bp + theme(axis.ticks=element_line(colour="#666666",size=2,linetype=1,lineend=2))

bp <- bp+theme(legend.position = c("top"),legend.title=element_blank(),
	legend.text = element_text(family = "myFont", size = 14),
	legend.direction="horizontal",
	#legend.background = element_rect(color = "#999999", fill = "grey90", size = 0.1, linetype = "solid")
	#legend.background = element_rect(color = "#999999", fill = alpha("blue", 0.1), size = 0.1, linetype = "solid")
	)
bp

