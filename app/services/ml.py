import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
X=np.array([[.05,.05,.1,.1],[.1,.15,.15,.2],[.2,.1,.25,.2],[.35,.3,.3,.25],[.5,.35,.45,.4],[.6,.55,.5,.5],[.75,.6,.65,.6],[.85,.8,.75,.7],[.15,.2,.1,.15],[.45,.5,.55,.45],[.7,.75,.8,.75],[.3,.25,.2,.3]])
Y=np.array([0,0,0,0,1,1,1,1,0,1,1,0])
MODEL=make_pipeline(StandardScaler(),LogisticRegression(random_state=7)).fit(X,Y)
def delay_prediction(*values):
    p=float(MODEL.predict_proba(np.array([values]))[0,1])
    return {"delay_probability":round(p,4),"risk_level":"high" if p>=.65 else "medium" if p>=.35 else "low","model":"Logistic regression trained on synthetic demo samples","warning":"Սինթետիկ տվյալներով demo մոդել է, ոչ արտադրական կանխատեսում։"}
def risk_rules(p):
    out=[]
    if p.progress_pct<20 and p.planned_days<60: out.append({"category":"schedule","severity":"high","score":.82,"description":"Կարճ ժամկետ և ցածր առաջընթաց․ վերանայել գրաֆիկը։"})
    if p.area_sqm>5000 and p.floors>10: out.append({"category":"complexity","severity":"medium","score":.62,"description":"Մեծ/բարձրահարկ նախագիծ․ պահանջվում է փուլային ռիսկերի կառավարում։"})
    if not out: out.append({"category":"monitoring","severity":"low","score":.18,"description":"Կանոնների հիման վրա կրիտիկական ազդանշան չկա․ շարունակել վերահսկումը։"})
    return out
