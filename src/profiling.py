"""Perfil de inferencia: tempo e alocacoes Python; consumo total de RAM requer psutil."""
import time
import tracemalloc
import numpy as np

def measure_inference(model, X, repeats=30):
    durations=[]
    tracemalloc.start()
    for _ in range(repeats):
        start=time.perf_counter()
        model.predict(X)
        durations.append(time.perf_counter()-start)
    _,peak=tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {'inference_mean_seconds':float(np.mean(durations)),
            'inference_sd_seconds':float(np.std(durations)),
            'inference_per_sample_ms':float(np.mean(durations)*1000/len(X)),
            'throughput_samples_second':float(len(X)/np.mean(durations)),
            'peak_tracemalloc_kb':peak/1024}
