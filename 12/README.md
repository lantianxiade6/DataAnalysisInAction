## 数据集成的两种架构：
- ETL(主流)   
多数据源数据->数据提取(Extract)-转换(Transform)-加载(Load)->数据仓库
- ELT(未来使用更多)   
多数据源数据->数据提取(Extract)-加载(Load)-转换(Transform)->数据仓库

工具：  
- 商业软件：Informatica PowerCenter,IBM InfoSphere DataStage,Oracle Data Integrator,Microsoft SQL Server Integration Services等
- 开源软件：Kettle,Talen,Apatar,Scriptella,DataX,Sqoop等  
Kettle下载地址：https://community.hitachivantara.com/docs/DOC-1009855