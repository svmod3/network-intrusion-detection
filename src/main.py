import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

from src.main import model_columns

app = FastAPI(title="System wykrywania anomalii sieciowych")

# ladowanie modelu
model = joblib.load("../notebooks/nsl_kdd_random_forest.joblib")
top_10_services = joblib.load("../notebooks/top_10_services.joblib")
model_columns = joblib.load("../notbooks/model_columns.joblib")


class NetworkTrafficInput(BaseModel):
    duration: int
    src_bytes: int
    dst_bytes: int
    land: int
    wrong_fragment: int
    urgent: int
    hot: int
    num_failed_logins: int
    logged_in: int
    num_compromised: int
    root_shell: int
    su_attempted: int
    num_root: int
    num_file_creations: int
    num_shells: int
    num_access_files: int
    is_host_login: int
    is_guest_login: int
    count: int
    srv_count: int
    serror_rate: float
    srv_serror_rate: float
    rerror_rate: float
    srv_rerror_rate: float
    same_srv_rate: float
    diff_srv_rate: float
    srv_diff_host_rate: float
    dst_host_count: int
    dst_host_srv_count: int
    dst_host_same_srv_rate: float
    dst_host_diff_srv_rate: float
    dst_host_same_src_port_rate: float
    dst_host_srv_diff_host_rate: float
    dst_host_serror_rate: float
    dst_host_srv_serror_rate: float
    dst_host_rerror_rate: float
    dst_host_srv_rerror_rate: float
    protocol_type: str
    service: str
    flag: str


@app.post("predict")
def predict_anomaly(data: NetworkTrafficInput):

    input_dict = data.dict()
    df = pd.DataFrame([input_dict])

    df["service"] = df["service"].apply(
        lambda x: x if x in top_10_services else "other"
    )

    df_encoded = pd.get_dummies(df, columns=["protocol_type", "flag", "service"])

    final_df = pd.DataFrame(columns=model_columns)

    final_df = pd.concat([final_df, df_encoded], axis=0).fillna(False)

    final_df = final_df[model_columns]
    prediction = model.predics(final_df)[0]

    result = "Anomalia (prawdpodobny atak)" if prediction == 1 else "Normalny Ruch"

    return {"status_code": 200, "prediction": int(prediction), "description": result}
