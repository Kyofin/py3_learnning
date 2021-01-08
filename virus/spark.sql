CREATE TEMPORARY VIEW v_city_feiyan_info
USING json
OPTIONS (path="file:///Users/huzekang/study/py3_learnning/out/2021-01-07/city_feiyan_info.txt");

CREATE TEMPORARY VIEW v_feiyan_track_info
USING json
OPTIONS (path="file:///Users/huzekang/study/py3_learnning/out/2021-01-07/feiyan_track_info.txt");

CREATE TEMPORARY VIEW v_foreign_feiyan_info
USING json
OPTIONS (path="file:///Users/huzekang/study/py3_learnning/out/2021-01-07/foreign_feiyan_info.txt");

CREATE TEMPORARY VIEW v_province_city_mapping
USING json
OPTIONS (path="file:///Users/huzekang/study/py3_learnning/out/2021-01-07/province_city_mapping.txt");

CREATE TEMPORARY VIEW v_province_feiyan_info
USING json
OPTIONS (path="file:///Users/huzekang/study/py3_learnning/out/2021-01-07/province_feiyan_info.txt");

insert overwrite  table city_feiyan_info partition(dt="2021-01-07") select * from v_city_feiyan_info;
insert overwrite  table feiyan_track_info partition(dt="2021-01-07") select * from v_feiyan_track_info;
insert overwrite  table foreign_feiyan_info partition(dt="2021-01-07") select * from v_foreign_feiyan_info;
insert overwrite  table province_city_mapping partition(dt="2021-01-07") select * from v_province_city_mapping;
insert overwrite  table province_feiyan_info partition(dt="2021-01-07") select * from v_province_feiyan_info;