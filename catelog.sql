USE catalogueDB;
CREATE TABLE catalogs(
    id                  INT                 NOT NULL    AUTO_INCREMENT,
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

    createdAt           DATETIME        	NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    updatedAt           DATETIME        	NOT NULL    DEFAULT CURRENT_TIMESTAMP,           
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
    id                  INT                 NOT NULL    AUTO_INCREMENT,
    name                VARCHAR(50)         NOT NULL,
    username            VARCHAR(50)         NOT NULL,   
    content             VARCHAR(500)        NOT NULL,

    createdAt           DATETIME        	NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    updatedAt           DATETIME        	NOT NULL    DEFAULT CURRENT_TIMESTAMP,   
    PRIMARY KEY( id )
);

CREATE TABLE tags_catalogs(
    id                  INT                 NOT NULL    AUTO_INCREMENT,
    tags_id             INT                 NOT NULL,
    catalogs_id         INT                 NOT NULL,

    createdAt           DATETIME        	NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    updatedAt           DATETIME        	NOT NULL    DEFAULT CURRENT_TIMESTAMP,   
    PRIMARY KEY( id )
)

CREATE TABLE users(
    id                  INT                 NOT NULL    AUTO_INCREMENT,
    username            VARCHAR(80)         NOT NULL,
    password            VARCHAR(120)        NOT NULL,
    email               VARCHAR(100)        NOT NULL,
    fullname            VARCHAR(80)         NOT NULL,

    createdAt           DATETIME        	NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    updatedAt           DATETIME        	NOT NULL    DEFAULT CURRENT_TIMESTAMP,      
    PRIMARY KEY( id )
);

INSERT INTO tags(username, name)
VALUES(
        "joycehsu", "系統"
);

INSERT INTO tags_catalogs(tag_id, catalog_id)VALUES("3", "4");

INSERT INTO tags
    (username, name)
VALUES(
        "joycehsu", "快穿"
);


INSERT INTO catalogs
    (username, book, author, end_date, introduction, review, category, tag, progress, article_source, author_link)
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

