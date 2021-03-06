# Generated by Django 3.0.1 on 2020-02-05 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cpf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50, verbose_name='Rua')),
                ('number', models.IntegerField(verbose_name='Numero')),
                ('complement', models.CharField(max_length=50, verbose_name='Complemento')),
                ('neighborhood', models.CharField(max_length=50, verbose_name='Bairro')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('state', models.CharField(max_length=50, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Gestor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Rg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rg', models.CharField(max_length=11, unique=True, verbose_name='RG')),
                ('shipping_date', models.DateField(verbose_name='Data de expedição')),
                ('dispatching_agency', models.CharField(max_length=10, verbose_name='Órgão expeditor')),
            ],
        ),
        migrations.CreateModel(
            name='TituloDeEleitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_de_eleitor', models.CharField(blank=True, max_length=12, unique=True, verbose_name='Titulo de eleitor')),
                ('zone', models.CharField(blank=True, max_length=12, verbose_name='Zona eleitoral')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('slug', models.SlugField(unique=True, verbose_name='Atalho')),
                ('date_of_birth', models.DateField(verbose_name='Data de nascimento')),
                ('sex', models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMININO')], max_length=1, verbose_name='Sexo')),
                ('children', models.CharField(choices=[('SIM', 'SIM'), ('NAO', 'NÃO')], max_length=3, verbose_name='Filhos')),
                ('amount_of_children', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0, verbose_name='Quantidade de filhos')),
                ('fathers_name', models.CharField(max_length=50, verbose_name='Nome do pai')),
                ('mothers_name', models.CharField(max_length=50, verbose_name='Nome da mãe')),
                ('degree_of_institution', models.CharField(max_length=31, verbose_name='Grau de instituição')),
                ('cargo', models.CharField(choices=[('TI', 'TI'), ('DIRETORIA', 'DIRETORIA'), ('RECURSOS HUMANOS', 'RECURSOS HUMANOS'), ('BACKOFFICE', 'BACKOFFICE'), ('SUPERVISOR', 'SUPERVISOR'), ('OPERADOR', 'OPERADOR')], max_length=17, verbose_name='Cargo')),
                ('adress', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.Endereco', verbose_name='Endereço')),
                ('cpf', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.Cpf', verbose_name='CPF')),
                ('rg', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.Rg', verbose_name='RG')),
                ('voter_title', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.TituloDeEleitor', verbose_name='Titulo de eleitor')),
            ],
        ),
    ]
