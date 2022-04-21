import ForwardStep
import backward_step


def testt(sample, isbais, wieghts, Activation_fn):
    all_nets = ForwardStep.forward(sample, isbais, wieghts, Activation_fn)
    encoded_out = backward_step.encode(all_nets[-1])
    return encoded_out
