import geopandas as gpd

korea = gpd.read_file("./KOR_adm/KOR_adm1.shp")

# korea.head(2)

# 전처리
korea["NL_NAME_1"] = korea["NL_NAME_1"].map(lambda x: x.split("|")[0].rstrip())
korea["VARNAME_1"] = korea["VARNAME_1"].map(lambda x: x.split("|")[0].rstrip())

# ISO 코드 변경( 지역마다 코드 부여 )
korea.loc[16, "ISO"] = "KR-31"  # 예시

# 변경된 파일 저장
out = "korea.shp"
seoul.to_file(out, encoding="utf-8")

