using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace C1
{
    public partial class Form1 : Form
    {
        public static int[] m = new int[0];
        public static Receiver alice;
        public static Sender bob;
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != "" && textBox2.Text != "") {
                alice = new Receiver(Convert.ToInt32(textBox1.Text), textBox2.Text);
                bob = new Sender(alice.getKeys());

                textBox3.Text = ""+alice.getP();
                textBox4.Text = alice.getFCode();
                textBox5.Text = ""+alice.getSumFCode();
                textBox6.Text = ""+alice.getQValue();
                textBox7.Text = ""+alice.co_value[0];
                textBox8.Text = ""+alice.getF_N();
                textBox9.Text = ""+alice.co_value[1];
                textBox10.Text = ""+alice.getDValue();
                
                textBox11.Text = ""+alice.co_value[1];
                textBox12.Text = ""+alice.co_value[0];
                textBox13.Text = ""+alice.co_value[0];
                textBox14.Text = ""+alice.getDValue();


            } else {
                MessageBox.Show("Заполните свой номер по списку группы и фамилию в соответствующие поля.");
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if(textBox11.Text != "" && textBox12.Text != "") {
                m = bob.send(richTextBox1.Text);
                richTextBox2.Text = "";
                richTextBox3.Text = "";
                foreach (int el in m) {
                    richTextBox2.Text += el + " ";
                    richTextBox3.Text += el + " ";
                }
            } else {
                MessageBox.Show("Заполните поле с открытым текстом сообщения, поля фамилии и номера по списку группы.");
            }
}

        private void button3_Click(object sender, EventArgs e)
        {
            if (textBox13.Text != "" && textBox14.Text != "") {
                richTextBox4.Text = alice.read(m);
            }
            else {
                MessageBox.Show("Заполните поле с открытым текстом сообщения, поля фамилии и номера по списку группы.");
            }
        }

        private void label15_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";
            textBox4.Text = "";
            textBox5.Text = "";
            textBox6.Text = "";
            textBox7.Text = "";
            textBox8.Text = "";
            textBox9.Text = "";
            textBox10.Text = "";
            textBox11.Text = "";
            textBox12.Text = "";
            textBox13.Text = "";
            textBox14.Text = "";

            richTextBox1.Text = "Введите открытый текст сообщения";
            richTextBox2.Text = "Ваш текст будет зашифрован";
            richTextBox3.Text = "Зашифрованный текст";
            richTextBox4.Text = "Ваш текст будет расшифрован";

            alice = null;
            bob = null;
            m = new int[0];
            MessageBox.Show("Выполнено: очистка полей.");
        }
    }
}