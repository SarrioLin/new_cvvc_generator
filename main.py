from email import generator
from cvvc_reclist_generator import CVVCReclistGenerator

def main():
    generator = CVVCReclistGenerator()
    
    generator.read_dict("dict_files\\CHN_extendForVS.txt")
    alias_union = generator.get_needed_alias(alias_config=".\\config\\alias_config.ini", is_cv_head=True, is_c_head=True)
    alias_union_backup = alias_union.copy()
    
    alias_union = generator.gen_plan_b(alias_union=alias_union)
    generator.gen_mora_x(alias_union=alias_union, length=8)
    
    generator.check_integrity(generator.get_needed_alias())
    generator.check_lsd_cvv_uniqueness()
    
    generator.gen_oto(alias_union_backup.copy(), 120)
    vs_alias_union = generator.get_needed_alias(alias_config=".\\config\\alias_config.ini", is_c_head=True, is_cv_head=True)
    generator.gen_vsdxmf(vs_alias_union.copy(), redirect_config_dir=".\\config\\redirect.ini", bpm=120)
    
    generator.save_oto("result\\oto.txt")
    generator.save_reclist("result\\reclist.txt")
    generator.save_presamp("result\\presamp.ini")
    generator.save_vsdxmf("result\\vsdxmf.vsdxmf")
    generator.save_lsd("result\\lsd.lsd")
    

if __name__ == "__main__":
    main()