

googFile <- 'C:/Users/admin/Downloads/LogisticRegression/GOOG.csv'
sp500File <- 'C:/Users/admin/Downloads/LogisticRegression/S&P500.csv'


# Example 2
# Preprocessing the data
goog <- read.table(googFile,header = TRUE, sep =",")[,c("Date","Adj.Close")]
names(goog)[2]<-"goog.price"
sp500 <- read.table(sp500File ,header = TRUE, sep =",")[,c("Date","Adj.Close")]
names(sp500)[2]<-"sp.price"

goog <- merge(goog, sp500, by = "Date")
goog[,c("Date")] <- as.Date(goog[,c("Date")],"%m/%d/%Y")
goog <- goog[order(goog$Date, decreasing = TRUE),]




goog[-nrow(goog),-1] <- goog[-nrow(goog),-1]/goog[-1,-1]-1
goog <- goog[-nrow(goog),]  
names(goog)[2:3] <- c("goog.returns","sp.returns")

combined <- data.frame(goog[-nrow(goog),],goog[-1,-1])
names(combined)[4:5] <- c("goog.lagged_1","sp.lagged_1")
 
combined$goog.UP = combined$goog.returns >= 0
fit <- glm(combined$goog.UP ~ combined$goog.lagged_1 + combined$sp.lagged_1,family=binomial())

results <- data.frame(combined$goog.UP,fitted(fit) >= 0.5)
names(results) <- c("Actual","PredictedByLogistic")
results$CorrectForecast = results$Actual == results$PredictedByLogistic

length(results$CorrectForecast[results$CorrectForecast == TRUE]) / length(results$CorrectForecast)

