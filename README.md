 WITH cob_afasta AS (select
          max(afa.ini_afa) as ini_afa,
          max(afa.fim_dem_afa) as fim_dem_afa,
          cod_mat
      from
          afastamento as afa,
          recebimento_atraso as ra
      where
          ra.id_rec_atr = ?
          and ( (afa.ini_afa between ini_ven_rec_atr and ter_ven_rec_atr)
          or (afa.fim_dem_afa between ini_ven_rec_atr and ter_ven_rec_atr))
      group by
          cod_mat)       , atraso AS        (  select
          ra.dat_hor_pro_rec_atr as dataprocessamento,
          cod_pes_ope_ite_rec_atr as matricula,
          cpf_dev_ite_rec_atr as cpf,
          nom_dev_ite_rec_atr as nome,
          b.id_pes as id_pes,
          sum(val_apu_ite_rec_atr) as valor,
          to_char(dat_com_ite_rec_atr,
          'MM/YYYY') as competencia,
          item.id_rec_atr as recebimento,
          item.dia_atr_ite_rec_atr as diasatraso
      from
          recebimento_atraso ra
      inner join
          item_recebimento_atraso item
              on item.id_rec_atr = ra.id_rec_atr
      inner join
          matricula m
              on m.cod_mat = item.cod_pes_ope_ite_rec_atr
      left join
          cob_afasta as ca
              on ca.cod_mat = m.cod_mat
      inner join
          beneficiario b
              on b.id_pes = m.id_pes
      where
          ra.id_rec_atr = ?
          and (  getexisteprodutoativo(cod_pes_ope_ite_rec_atr) = ?
          or  (ca.cod_mat is not null
          and  getexisteprodutoativo(cod_pes_ope_ite_rec_atr) = ?)  )
      group by
          item.id_rec_atr,
          ra.dat_hor_pro_rec_atr,
          cod_pes_ope_ite_rec_atr,
          cpf_dev_ite_rec_atr,
          nom_dev_ite_rec_atr,
          b.id_pes ,
          competencia,
          diasatraso,
          ra.id_rec_atr
      having
          sum(item.dia_atr_ite_rec_atr) >= 50  ),   jurosemulta as (    select
          tjm.*
      from
          tabela_juros_multa tjm
      where
          1 between tjm.par_ini_tab_jur_mul and tjm.par_fin_tab_jur_mul
          and current_date >= tjm.vig_tab_jur_mul
      order by
          tjm.vig_tab_jur_mul desc    limit 1   ),   menoradesao as (   select
          min(ini_ade) as primeiraadesao,
          cod_mat
      from
          view_adesao_atual vaa
      group by
          cod_mat)  select
          *
      from
          (       select
              dataprocessamento,
              matricula,
              cpf,
              nome,
              atraso.id_pes,
              sum(valor),
              competencia,
              COUNT(competencia) OVER (partition
          by
              id_pes) as tipo,
              recebimento,
              diasatraso,
              trunc(        sum(valor) +     + sum(valor) * (j.mul_tab_jur_mul / 100)      + sum(valor) * (j.jur_ad_tab_jur_mul / 100) * diasatraso,
              2    ) as valortotalcomencargos,
              primeiraadesao
          from
              atraso
          inner join
              menoradesao
                  on   menoradesao.cod_mat = atraso.matricula    cross
          join
              jurosemulta j
          group by
              dataprocessamento,
              matricula,
              cpf,
              nome,
              atraso.id_pes,
              competencia,
              recebimento,
              diasatraso,
              j.mul_tab_jur_mul,
              j.jur_ad_tab_jur_mul,
              primeiraadesao
          order by
              nome,
              cpf) as x
      where
          1=1
