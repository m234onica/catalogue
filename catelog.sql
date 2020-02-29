USE catalogueDB;
CREATE TABLE catalogs(
    id                  INT                 NOT NULL    AUTO_INCREMENT,
    createdAt           DATETIME        	NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    updatedAt           DATETIME        	NOT NULL    DEFAULT CURRENT_TIMESTAMP,           
    username            VARCHAR(50)         NOT NULL,
    book                VARCHAR(100)        NOT NULL,
    author              VARCHAR(100)        NOT NULL,
    end_date            DATE,
    introduction        VARCHAR(1000)       NOT NULL,
    review              FLOAT(1),
    category            VARCHAR(50),
    tag                 VARCHAR(50),
    progress            Enum("tbc", "extra", "end"),
    article_source      VARCHAR(500),
    author_link         VARCHAR(500),
    PRIMARY KEY( id )
);

CREATE TABLE comments(
    id                  INT                 NOT NULL    AUTO_INCREMENT,
    username            VARCHAR(50)         NOT NULL,
    review              FLOAT(1),
    content             VARCHAR(6000)       NOT NULL,
    createdAt           DATETIME        	NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    updatedAt           DATETIME        	NOT NULL    DEFAULT CURRENT_TIMESTAMP,      
    PRIMARY KEY( id )
)

CREATE TABLE tags(
    name                VARCHAR(50)         NOT NULL,
    createdAt           DATETIME        	NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    updatedAt           DATETIME        	NOT NULL    DEFAULT CURRENT_TIMESTAMP,   
    username            VARCHAR(50)         NOT NULL,   
    content             VARCHAR(500)        NOT NULL,
    PRIMARY KEY( name )
);

CREATE TABLE users(
    id                  INT                 NOT NULL    AUTO_INCREMENT,
    username            VARCHAR(80)         NOT NULL,
    password            VARCHAR(120)        NOT NULL,
    createdAt           DATETIME        	NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    updatedAt           DATETIME        	NOT NULL    DEFAULT CURRENT_TIMESTAMP,      
    email               VARCHAR(100)        NOT NULL,
    fullname            VARCHAR(80)         NOT NULL,
    PRIMARY KEY( id )
);

INSERT INTO tags(name, content)
VALUES(
        "無限流", "《無限流》起源於小說《無限恐怖》的火爆，以及大量跟風小說的問世。 無限流意義應該是'包羅萬象'，即：包含無限的元素，包括科學、宗教、神話、傳說、歷史、現實、電影、動漫、遊戲等，並且高於它們，有這樣包含這一切的世界觀才是無限流小說的精華。"
);

INSERT INTO catalogs
    (fullname, book, author, end_date, introduction, review, category, tag, progress, article_source, author_link)
VALUES(
        "joychsu",
        "不要在垃圾桶裡撿男朋友",
        "騎鯨南去",
        "2018-05-02",
        "池小池，四流出身，三料影帝，二流脾性，一品相貌，從地獄hard模式一路洗牌通關至人生贏家模式。
  然後，他被一盞吊燈砸成了植物人模式。
  061：你好，渣攻回收系統了解一下。本系統以渣攻的悔意值為計量單位，每積攢一百悔意值即可脫離當前世界。友情提示一下，我們的員工在工作中一般是通過自我奉獻與犧牲，培養渣攻的依賴性，一步步讓渣攻離不開……
  池小池：身敗名裂算多少後悔值？跌落神壇算多少後悔值？求而不得算多少後悔值？
  061：……",
        "6.0",
        "現代",
        "快穿",
        "end",
        "http://www.jjwxc.net/onebook.php?novelid=3511075",
        "http://www.jjwxc.net/oneauthor.php?authorid=2136709"
);

INSERT INTO comments(fullname, review, catalog_id, content)
VALUES(
    "joycehsu",
    "4.5",
    "1",
    "好看！"
);

