USE catalogueDB;
CREATE TABLE catalogs(
  id                  INT             NOT NULL    AUTO_INCREMENT,
  createdAt           TIMESTAMP       NOT NULL    DEFAULT CURRENT_TIMESTAMP(),
  book                VARCHAR(100)    NOT NULL,
  author              VARCHAR(100)    NOT NULL,
  end_date            DATE,
  introduction        VARCHAR(1000)   NOT NULL,
  review              FLOAT(1),
  category            VARCHAR(50),
  tag                 VARCHAR(50),
  progress            BOOLEAN,
  article_source      VARCHAR(500),
  author_link         VARCHAR(500),
  PRIMARY KEY( id )
);

CREATE TABLE comments(
  id                  INT             NOT NULL    AUTO_INCREMENT,
  fullname              VARCHAR(100)    NOT NULL,
  review              FLOAT(1),
  content             VARCHAR(6000)   NOT NULL,
  createdAt           TIMESTAMP       NOT NULL    DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY( id )
)

CREATE TABLE tags(
  id                  INT             NOT NULL    AUTO_INCREMENT,
  createdAt           TIMESTAMP       NOT NULL    DEFAULT CURRENT_TIMESTAMP(),
  content             VARCHAR(6000)   NOT NULL,
  PRIMARY KEY( id )
);
