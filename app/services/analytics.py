from app.schemas import Estimate
BASE={"residential":280000,"commercial":330000,"industrial":240000,"renovation":160000}
FINISH={"basic":.88,"standard":1.0,"premium":1.22}
def estimate(x:Estimate):
    direct=x.area_sqm*BASE.get(x.building_type,BASE["residential"])*FINISH.get(x.finish_level,1)*(1+max(x.floors-1,0)*.012)
    contingency=direct*x.contingency_pct/100
    return {"currency":"AMD","area_sqm":x.area_sqm,"materials_amd":round(direct*.58,2),"labor_amd":round(direct*.27,2),"equipment_amd":round(direct*.08,2),"other_amd":round(direct*.07,2),"contingency_amd":round(contingency,2),"estimated_total_amd":round(direct+contingency,2),"cost_per_sqm_amd":round((direct+contingency)/x.area_sqm,2),"assumptions":"Indicative demo coefficients only; not a quotation or bill of quantities."}
def optimize(budget,cost):
    gap=budget-cost
    return {"status":"within_budget" if gap>=0 else "over_budget","gap_amd":round(abs(gap),2),"suggestions":[{"action":"Համեմատել առնվազն 3 մատակարարի ամբողջական առաջարկները","potential_saving_pct":2},{"action":"Վերանայել ոչ կրիտիկական հարդարման տարբերակները","potential_saving_pct":3},{"action":"Պլանավորել փուլային գնումներ՝ պահեստավորման ծախսը վերահսկելով","potential_saving_pct":2}]}
