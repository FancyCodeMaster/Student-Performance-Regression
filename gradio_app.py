import gradio as gr
from prediction import predict_performance

# Create the Gradio interface
iface = gr.Interface(
    fn=predict_performance,
    inputs=[
        gr.Number(label="Hours Studied : (min:0, max:8)", value=0, precision=0, minimum=0, maximum=8),
        gr.Number(label="Previous Scores : (min:0, max:100)", value=1, precision=0, minimum=0, maximum=100),
        gr.Checkbox(label="Participated in Extracurricular Activities"),
        gr.Number(label="Sleep Hours : (min:0, max:8)", value=0, precision=0, minimum=0, maximum=8),
        gr.Number(label="Sample Questions Practised : (min:0, max:60)", value=0.0, precision=0, minimum=0, maximum=60)
    ],
    outputs="text",
    title="Student Performance Predictor",
    description="Predict a student's performance based on study habits, previous scores, and more."
)

if __name__ == "__main__":
    # Launch the app
    iface.launch(share=True)
