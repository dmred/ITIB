#pragma once
#include <vector>
#include <iostream>
#include <string>

class Neuron
{
public:
	Neuron();
	Neuron(double w00, double w01, double w03, double w10, double w11, double w20, double w21);
	~Neuron();

	double func_f(double net);
	double func_df(double f);
	int study_neuron();
	
	std::vector<double> W0{ 0,0,0 }; // Çíŕ÷ĺíč˙ âĺńîâűő ęîýôôčöčĺíňîâ ďî óěîë÷ŕíčţ
	std::vector<double> W01{ 0,0 }; // Çíŕ÷ĺíč˙ âĺńîâűő ęîýôôčöčĺíňîâ ďî óěîë÷ŕíčţ
	std::vector<double> W02{ 0,0 }; // Çíŕ÷ĺíč˙ âĺńîâűő ęîýôôčöčĺíňîâ ďî óěîë÷ŕíčţ

	std::vector<double> t{ -0.1, - 0.1 }; // Çíŕ÷ĺíčĺ öĺëĺâîăî âĺęňîđŕ
	std::vector<double> x{ 1,2,1 }; // Çíŕ÷ĺíčĺ âőîäíîăî âĺęňîđŕ 
	double E = 0.001; // Ďîđîă ńđĺäíĺęâŕäđŕňč÷íîé îřčáęč
	double n = 0.66; // Íîđěŕ îáó÷ĺíč˙
};

Neuron::Neuron() {}

Neuron::Neuron(double w00, double w01, double w02, double w10, double w11, double w20, double w21 ) { // Çàäàåì íà÷àëüíûå çíà÷åíèå âåêòîðà âåñîâ
	W0[0] = w00;
	W0[1] = w01;
	W0[2] = w02;
	W01[0] = w10;
	W01[1] = w11;
	W02[0] = w20;
	W02[1] = w21;
}

Neuron::~Neuron() {}

double Neuron::func_f(double net) { // Ôóíêöèÿ àêòèâàöèè íåéðîíîâ
	double f = (1 - exp(-net)) / (1 + exp(-net));
	return f;
}

double Neuron::func_df(double f) { // Ïðîèçâîäíàÿ ôóíêöèè àêòèâàöèè
	double df = (1 - f * f) / 2;
	return df;
}

int Neuron::study_neuron() { // Îáó÷åíèå íåéðîííîé ñåòè
	int k = 0; // Íîìåð ýïîõè
	double net0, net01, net02, xj, y01, y02;
	double delta0, delta01, delta02;
	std::vector<double> delta_w0{ 0,0,0 };
	std::vector<double> delta_w01{ 0,0 };
	std::vector<double> delta_w02{ 0,0 };


	while (k < 2000) {
		// Ðàñ÷åò âûõîäà íåéðîííîé ñåòè
		net0=W0[0];
		for (size_t i = 1; i < W0.size(); i++) {
			net0 += W0[i] * x[i];
		}
		xj = func_f(net0);
		net01 = W01[1] * xj + W01[0];
		net02 = W02[1] * xj + W02[0];
		y01 = func_f(net01);
		y02 = func_f(net02);

		double Er = sqrt(pow((t[0] - y01), 2) + pow((t[1] - y02), 2));
		if (Er < E) break;
		std::cout << "k = " << k << "  E = " << Er << "  y = ( " << y01 << " " << y02 << " )" << std::endl;

		// Îáó÷åíèå ñ ó÷èòåëåì
		delta01 = func_df(net01)*(t[0] - y01);
		delta02 = func_df(net02)*(t[1] - y02);
		delta0 = func_df(net0)*(delta01*W01[1] + delta02 * W02[1]);
		for (size_t i = 0; i < delta_w0.size(); i++) {
			delta_w0[i] = n * x[i] * delta0;
		}
		delta_w01[0] = n * delta01;
		delta_w02[0] = n * delta02;
		delta_w01[1] = n * xj * delta01;
		delta_w02[1] = n * xj * delta02;
		for (size_t i = 0; i < delta_w0.size(); i++) {
			W0[i] += delta_w0[i];
		}
		for (size_t i = 0; i < delta_w01.size(); i++) {
			W01[i] += delta_w01[i];
			W02[i] += delta_w02[i];
		}
		k++;
	}
	return k;	
}



int main(int argc, char *argv[]) {
	Neuron neur;
	neur.study_neuron();

	int pause;
	std::cin >> pause;
	return 0;
}